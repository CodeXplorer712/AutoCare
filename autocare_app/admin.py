from django.contrib import admin
from .models import Service, Product, ContactMessage


# Service Admin Configuration
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')  # Columns to display in admin list
    search_fields = ('name', 'description')  # Enable search by name and description
    list_filter = ('created_at',)  # Filter by creation date


# Product Admin Configuration
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')  # Columns to display in admin list
    search_fields = ('name', 'description')  # Enable search by name and description
    list_filter = ('created_at',)  # Filter by creation date


# ContactMessage Admin Configuration
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')  # Columns to display in admin list
    search_fields = ('name', 'email', 'message')  # Enable search
    list_filter = ('created_at',)  # Filter by creation date
    readonly_fields = ('created_at',)  # Make timestamp read-only

