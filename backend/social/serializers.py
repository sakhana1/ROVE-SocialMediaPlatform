from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile,Post,Comment,Follow,Bookmark,Collection,DirectMessage,Notification,Block,Report,SupportRequest
class UserSerializer(serializers.ModelSerializer):
    display_name=serializers.SerializerMethodField(); avatar=serializers.SerializerMethodField(); bio=serializers.SerializerMethodField()
    class Meta: model=User; fields=['id','username','first_name','last_name','email','display_name','avatar','bio']
    def get_display_name(self,obj): return getattr(getattr(obj,'profile',None),'display_name','') or obj.get_full_name() or obj.username
    def get_avatar(self,obj):
        p=getattr(obj,'profile',None)
        if p and p.avatar: return self.context['request'].build_absolute_uri(p.avatar.url) if self.context.get('request') else p.avatar.url
        return ''
    def get_bio(self,obj): return getattr(getattr(obj,'profile',None),'bio','')
class ProfileSerializer(serializers.ModelSerializer):
    username=serializers.CharField(source='user.username',read_only=True); email=serializers.EmailField(source='user.email',read_only=True)
    display_name=serializers.CharField(required=False,allow_blank=True)
    class Meta: model=Profile; fields=['username','email','display_name','bio','website','avatar','is_private','comment_permission','mention_permission','show_activity_status']; read_only_fields=['username','email']
class CommentSerializer(serializers.ModelSerializer):
    username=serializers.CharField(source='author.username',read_only=True)
    class Meta: model=Comment; fields=['id','username','text','created_at']
class PostSerializer(serializers.ModelSerializer):
    username=serializers.CharField(source='author.username',read_only=True); display_name=serializers.SerializerMethodField(); avatar=serializers.SerializerMethodField(); image=serializers.SerializerMethodField(); likes_count=serializers.IntegerField(source='likes.count',read_only=True); comments_count=serializers.IntegerField(source='comments.count',read_only=True); comments=CommentSerializer(many=True,read_only=True); is_liked=serializers.SerializerMethodField(); is_bookmarked=serializers.SerializerMethodField()
    image_upload=serializers.ImageField(source='image',write_only=True,required=False)
    class Meta: model=Post; fields=['id','username','display_name','avatar','image','image_upload','image_url','caption','location','created_at','updated_at','likes_count','comments_count','comments','is_liked','is_bookmarked']
    def get_display_name(self,obj): return obj.author.get_full_name() or obj.author.username
    def get_avatar(self,obj):
        p=getattr(obj.author,'profile',None)
        if p and p.avatar: return self.context['request'].build_absolute_uri(p.avatar.url)
        return ''
    def get_image(self,obj):
        if obj.image: return self.context['request'].build_absolute_uri(obj.image.url)
        return obj.image_url
    def get_is_liked(self,obj):
        u=self.context['request'].user
        return bool(u.is_authenticated and obj.likes.filter(user=u).exists())
    def get_is_bookmarked(self,obj):
        u=self.context['request'].user
        return bool(u.is_authenticated and Bookmark.objects.filter(user=u,post=obj).exists())
class CollectionSerializer(serializers.ModelSerializer):
    posts=serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    class Meta: model=Collection; fields=['id','name','description','is_private','posts','created_at']
class MessageSerializer(serializers.ModelSerializer):
    sender=serializers.CharField(source='sender.username',read_only=True); recipient=serializers.CharField(source='recipient.username',read_only=True)
    class Meta: model=DirectMessage; fields=['id','sender','recipient','text','created_at','is_read']
class NotificationSerializer(serializers.ModelSerializer):
    actor=serializers.CharField(source='actor.username',read_only=True)
    class Meta: model=Notification; fields=['id','actor','kind','post_id','text','is_read','created_at']
