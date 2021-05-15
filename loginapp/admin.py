from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    search_fields = ['name']


# Register your models here.
admin.site.register(User,UserAdmin) # admin에 User 검색 기능 추가
