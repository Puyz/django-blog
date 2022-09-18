from django.contrib import admin
from blogapp.models import BlogPost, Category, SubCategory, Message


admin.site.register(BlogPost)
admin.site.register(SubCategory)
admin.site.register(Category)
admin.site.register(Message)