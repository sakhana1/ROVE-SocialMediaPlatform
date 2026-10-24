from django.contrib import admin
from .models import Profile,Post,Comment,Like,Follow,Bookmark,Collection,DirectMessage,Notification,Block,Report,SupportRequest
admin.site.register([Profile,Post,Comment,Like,Follow,Bookmark,Collection,DirectMessage,Notification,Block,Report,SupportRequest])
