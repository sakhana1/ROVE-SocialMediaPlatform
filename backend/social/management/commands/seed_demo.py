from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from social.models import Profile,Post,Comment
class Command(BaseCommand):
    help='Create safe sample ROVE users and posts for local development.'
    def handle(self,*args,**kwargs):
        samples=[
          ('elena_rove','Elena Rivera','https://images.unsplash.com/photo-1470770841072-f978cf4d019e?auto=format&fit=crop&w=1200&q=85','Somewhere between the mountains and the morning light. ✨ #slowtravel #nature','Dolomites, Italy'),
          ('marcus.lind','Marcus Lindqvist','https://images.unsplash.com/photo-1500530855697-b586d89ba3ee?auto=format&fit=crop&w=1200&q=85','Finding the quiet corners of the city.','Copenhagen, Denmark'),
          ('maya.frames','Maya Chen','https://images.unsplash.com/photo-1518837695005-2083093ee35b?auto=format&fit=crop&w=1200&q=85','Ocean air, no plans. #coastalliving','Amalfi Coast'),
        ]
        for username,name,url,caption,location in samples:
            user,created=User.objects.get_or_create(username=username,defaults={'first_name':name,'email':f'{username.replace(".","_")}@example.local'})
            if created:user.set_unusable_password();user.save()
            Profile.objects.get_or_create(user=user,defaults={'display_name':name,'bio':'Collecting moments and stories worth sharing.'})
            Post.objects.get_or_create(author=user,caption=caption,defaults={'image_url':url,'location':location})
        self.stdout.write(self.style.SUCCESS('ROVE demo users and posts are ready.'))
