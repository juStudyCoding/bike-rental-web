from django.contrib import admin

# Register your models here.
from .models import Notice

class NoticeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')

admin.site.register(Notice,NoticeAdmin)
