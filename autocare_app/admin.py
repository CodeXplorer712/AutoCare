from django.contrib import admin
from .models import CarWashBooking, ServiceBooking


# CarWashBooking Admin Configuration
@admin.register(CarWashBooking)
class CarWashBookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'phone', 'car_number', 'address', 'wash_package', 'booking_date', 'booking_time', 'created_at')
    search_fields = ('customer_name', 'phone', 'car_number', 'address')
    list_filter = ('wash_package', 'booking_date', 'created_at')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)  # Most recent bookings first


# ServiceBooking Admin Configuration
@admin.register(ServiceBooking)
class ServiceBookingAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'phone', 'car_number', 'address', 'service_category', 'booking_date', 'booking_time', 'created_at')
    search_fields = ('customer_name', 'phone', 'car_number', 'address')
    list_filter = ('service_category', 'booking_date', 'created_at')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)  # Most recent bookings first

