from django.contrib import admin
from .models import *

# admin.site.register([CustomUserRegistration])

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    fields = ('name','mobile',)

@admin.register(CustomUserRegistration)
class CustomUserRegistrationAdmin(admin.ModelAdmin):
    fields = ('name', 'shop_name')
    search_fields = ('name', 'shop_name',)
    # list_filter = ('created_at',)
    list_display = ('name', 'shop_name',)
    # ordering = ('-created_at',)