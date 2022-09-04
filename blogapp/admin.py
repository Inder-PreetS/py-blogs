from django.contrib import admin
from blogapp.models import Blog, Likes, Tag
# Register your models here.


admin.site.register((Blog, Tag, Likes))