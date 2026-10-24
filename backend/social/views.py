from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db.models import Q
from rest_framework import generics,permissions,status,viewsets
from rest_framework.decorators import api_view,permission_classes,parser_classes
from rest_framework.parsers import MultiPartParser,FormParser,JSONParser
from rest_framework.response import Response
from rest_framework.exceptions import NotAuthenticated, PermissionDenied
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Profile,Post,Comment,Like,Follow,Bookmark,Collection,DirectMessage,Notification,Block,Report,SupportRequest
from .serializers import UserSerializer,ProfileSerializer,PostSerializer,CommentSerializer,CollectionSerializer,MessageSerializer,NotificationSerializer

def profile_for(user):
    profile,created=Profile.objects.get_or_create(user=user,defaults={'display_name':user.get_full_name()})
    return profile
@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    username=(request.data.get('username') or '').strip(); email=(request.data.get('email') or '').strip(); password=request.data.get('password') or ''; name=(request.data.get('first_name') or request.data.get('name') or '').strip()
    if not username or not email or not password: return Response({'detail':'Username, email and password are required.'},status=400)
    if User.objects.filter(username__iexact=username).exists(): return Response({'detail':'That username is already taken.'},status=400)
    if User.objects.filter(email__iexact=email).exists(): return Response({'detail':'An account with that email already exists.'},status=400)
    try: validate_password(password)
    except ValidationError as e: return Response({'detail':' '.join(e.messages)},status=400)
    user=User.objects.create_user(username=username,email=email,password=password,first_name=name)
    profile_for(user)
    refresh=RefreshToken.for_user(user)
    return Response({'access':str(refresh.access_token),'refresh':str(refresh),'user':UserSerializer(user,context={'request':request}).data},status=201)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def me(request):
    profile_for(request.user)
    data=UserSerializer(request.user,context={'request':request}).data
    return Response(data)
@api_view(['POST'])
@permission_classes([AllowAny])
def password_reset(request):
    # Generic response avoids disclosing whether an account exists. Actual email delivery requires configuration.
    return Response({'detail':'If an account matches that email, recovery instructions will be sent.'})
class PostViewSet(viewsets.ModelViewSet):
    serializer_class=PostSerializer
    parser_classes=[MultiPartParser,FormParser,JSONParser]
    def get_queryset(self): return Post.objects.select_related('author').prefetch_related('likes','comments').order_by('-created_at')
    def perform_create(self,serializer):
        if not self.request.user.is_authenticated: raise NotAuthenticated('Please log in to publish a post.')
        serializer.save(author=self.request.user)
    def perform_update(self,serializer):
        if self.get_object().author_id!=self.request.user.id: raise PermissionDenied('You can only edit your own posts.')
        serializer.save()
    def perform_destroy(self,instance):
        if instance.author_id!=self.request.user.id: raise PermissionDenied('You can only delete your own posts.')
        instance.delete()
@api_view(['POST'])
def like_post(request,pk):
    if not request.user.is_authenticated: return Response({'detail':'Please log in to like posts.'},status=401)
    post=Post.objects.filter(pk=pk).first()
    if not post:return Response({'detail':'Post not found.'},status=404)
    like,created=Like.objects.get_or_create(post=post,user=request.user)
    if not created: like.delete(); liked=False
    else:
        liked=True
        if post.author_id!=request.user.id: Notification.objects.create(recipient=post.author,actor=request.user,kind='like',post=post,text='liked your post')
    return Response({'liked':liked,'likes_count':post.likes.count()})
@api_view(['POST'])
def bookmark_post(request,pk):
    if not request.user.is_authenticated:return Response({'detail':'Please log in to save posts.'},status=401)
    post=Post.objects.filter(pk=pk).first()
    if not post:return Response({'detail':'Post not found.'},status=404)
    obj,created=Bookmark.objects.get_or_create(user=request.user,post=post)
    if not created:obj.delete()
    return Response({'bookmarked':created})
@api_view(['GET','POST'])
def post_comments(request,pk):
    post=Post.objects.filter(pk=pk).first()
    if not post:return Response({'detail':'Post not found.'},status=404)
    if request.method=='GET': return Response(CommentSerializer(post.comments.select_related('author').all(),many=True).data)
    if not request.user.is_authenticated:return Response({'detail':'Please log in to comment.'},status=401)
    text=(request.data.get('text') or '').strip()
    if not text:return Response({'detail':'Comment cannot be empty.'},status=400)
    comment=Comment.objects.create(post=post,author=request.user,text=text)
    if post.author_id!=request.user.id:Notification.objects.create(recipient=post.author,actor=request.user,kind='comment',post=post,text=text[:220])
    return Response(CommentSerializer(comment).data,status=201)
@api_view(['GET','PATCH','PUT'])
@parser_classes([MultiPartParser,FormParser,JSONParser])
def profile_detail(request,username):
    user=request.user if username=='me' and request.user.is_authenticated else User.objects.filter(username=username).first()
    if not user:return Response({'detail':'Profile not found.'},status=404)
    p=profile_for(user)
    if request.method in ('PATCH','PUT'):
        if not request.user.is_authenticated or request.user.id!=user.id:return Response({'detail':'You can only edit your own profile.'},status=403)
        s=ProfileSerializer(p,data=request.data,partial=True,context={'request':request});s.is_valid(raise_exception=True);s.save()
        if 'first_name' in request.data: user.first_name=request.data['first_name'];user.save(update_fields=['first_name'])
        return Response(s.data)
    data=ProfileSerializer(p,context={'request':request}).data
    data.update({'posts_count':user.posts.count(),'followers_count':user.follower_links.count(),'following_count':user.following_links.count(),'display_name':p.display_name or user.get_full_name() or user.username,'username':user.username})
    return Response(data)
@api_view(['GET','POST'])
def follows(request):
    if not request.user.is_authenticated:return Response({'detail':'Please log in to follow people.'},status=401)
    if request.method=='GET': return Response([{'username':f.following.username} for f in Follow.objects.filter(follower=request.user).select_related('following')])
    username=request.data.get('username')
    target=User.objects.filter(username=username).first()
    if not target:return Response({'detail':'User not found.'},status=404)
    if target==request.user:return Response({'detail':'You cannot follow yourself.'},status=400)
    obj,created=Follow.objects.get_or_create(follower=request.user,following=target)
    if not created:obj.delete();following=False
    else:
        following=True;Notification.objects.create(recipient=target,actor=request.user,kind='follow',text='started following you')
    return Response({'following':following})
@api_view(['GET'])
def bookmarks(request):
    if not request.user.is_authenticated:return Response({'detail':'Please log in to view saved posts.'},status=401)
    qs=Post.objects.filter(bookmark__user=request.user).order_by('-bookmark__created_at')
    return Response(PostSerializer(qs,many=True,context={'request':request}).data)
class CollectionViewSet(viewsets.ModelViewSet):
    serializer_class=CollectionSerializer; permission_classes=[IsAuthenticated]
    def get_queryset(self):return Collection.objects.filter(user=self.request.user).order_by('-created_at')
    def perform_create(self,serializer):serializer.save(user=self.request.user)
@api_view(['GET','POST'])
def messages(request):
    if not request.user.is_authenticated:return Response({'detail':'Please log in to use messages.'},status=401)
    if request.method=='GET':
        qs=DirectMessage.objects.filter(Q(sender=request.user)|Q(recipient=request.user)).order_by('created_at')
        return Response(MessageSerializer(qs,many=True).data)
    recipient=User.objects.filter(username=request.data.get('recipient')).first(); text=(request.data.get('text') or '').strip()
    if not recipient or not text:return Response({'detail':'A valid recipient and message are required.'},status=400)
    obj=DirectMessage.objects.create(sender=request.user,recipient=recipient,text=text)
    return Response(MessageSerializer(obj).data,status=201)
@api_view(['GET','POST'])
def notifications(request):
    if not request.user.is_authenticated:return Response({'detail':'Please log in to view notifications.'},status=401)
    if request.method=='POST':Notification.objects.filter(recipient=request.user).update(is_read=True);return Response({'marked_read':True})
    return Response(NotificationSerializer(request.user.notifications.select_related('actor').all(),many=True).data)
@api_view(['GET','PATCH'])
def privacy(request):
    if not request.user.is_authenticated:return Response({'detail':'Please log in to manage privacy settings.'},status=401)
    p=profile_for(request.user)
    if request.method=='PATCH':
        s=ProfileSerializer(p,data=request.data,partial=True,context={'request':request});s.is_valid(raise_exception=True);s.save();return Response(s.data)
    return Response(ProfileSerializer(p,context={'request':request}).data)
@api_view(['GET','POST','DELETE'])
def blocked(request,username=None):
    if not request.user.is_authenticated:return Response({'detail':'Please log in to manage blocked accounts.'},status=401)
    if request.method=='GET':return Response([{'username':b.blocked.username,'display_name':b.blocked.get_full_name() or b.blocked.username} for b in Block.objects.filter(blocker=request.user).select_related('blocked')])
    if request.method=='POST':
        target=User.objects.filter(username=request.data.get('username')).first()
        if not target:return Response({'detail':'User not found.'},status=404)
        Block.objects.get_or_create(blocker=request.user,blocked=target);return Response({'blocked':True},status=201)
    Block.objects.filter(blocker=request.user,blocked__username=username).delete();return Response(status=204)
@api_view(['POST'])
def create_report(request):
    Report.objects.create(user=request.user if request.user.is_authenticated else None,report_type=request.data.get('report_type','content'),category=request.data.get('category',''),reason=request.data.get('reason',''),title=request.data.get('title',''),details=request.data.get('details',''))
    return Response({'detail':'Report submitted successfully.'},status=201)
@api_view(['POST'])
def support(request):
    required=['name','email','subject','message']
    if any(not request.data.get(k) for k in required):return Response({'detail':'Name, email, subject and message are required.'},status=400)
    SupportRequest.objects.create(user=request.user if request.user.is_authenticated else None,name=request.data['name'],email=request.data['email'],category=request.data.get('category',''),subject=request.data['subject'],message=request.data['message'])
    return Response({'detail':'Support request submitted.'},status=201)
