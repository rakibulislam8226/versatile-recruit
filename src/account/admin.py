from django.contrib import admin
from .models import CustomUser
# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username' ,'email', 'phone', 'role', 'is_active')
    list_editable = ('is_active',)
    search_fields = ( 'email', 'phone')
    list_filter = ('groups', 'is_active')