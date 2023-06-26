from django.contrib import admin
from .models import CustomUser
# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username' ,'email', 'phone', 'role')
    search_fields = ( 'email', 'phone')
    list_filter = ('groups',)