from django.contrib import admin

from blog.models import *
# Register your models here.

admin.site.register(Folder)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(MCQ)
admin.site.register(CQ)
admin.site.register(Path)
