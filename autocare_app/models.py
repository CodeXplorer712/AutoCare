from django.db import models

# CarWashBooking Model - Stores car wash booking information
class CarWashBooking(models.Model):
    PACKAGE_CHOICES = [
        ('basic', 'Basic Wash - ₹299'),
        ('premium', 'Premium Wash - ₹599'),
        ('deluxe', 'Deluxe Detailing - ₹999'),
    ]
    
    customer_name = models.CharField(max_length=100, help_text="Customer's full name")
    phone = models.CharField(max_length=15, help_text="Customer's phone number")
    car_number = models.CharField(max_length=20, help_text="Vehicle registration number")
    address = models.TextField(help_text="Customer's address for car pickup/delivery")
    wash_package = models.CharField(max_length=20, choices=PACKAGE_CHOICES, help_text="Selected wash package")
    booking_date = models.DateField(help_text="Preferred service date")
    booking_time = models.TimeField(help_text="Preferred service time")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.customer_name} - {self.get_wash_package_display()} on {self.booking_date}"
    
    class Meta:
        ordering = ['-created_at']  # Most recent first


# ServiceBooking Model - Stores service booking information from services page
class ServiceBooking(models.Model):
    SERVICE_CATEGORY_CHOICES = [
        ('basic-maintenance', 'Basic Maintenance'),
        ('mechanical-repairs', 'Mechanical Repairs'),
        ('electrical-electronics', 'Electrical & Electronics'),
        ('ac-climate-control', 'AC & Climate Control'),
        ('tyre-wheel', 'Tyre & Wheel'),
        ('inspection-diagnostics', 'Inspection & Diagnostics'),
        ('pre-delivery-inspection', 'Pre-Delivery Inspection'),
    ]
    
    customer_name = models.CharField(max_length=100, help_text="Customer's full name")
    phone = models.CharField(max_length=15, help_text="Customer's phone number")
    car_number = models.CharField(max_length=20, help_text="Vehicle registration number")
    address = models.TextField(help_text="Customer's address for service location")
    service_category = models.CharField(max_length=50, choices=SERVICE_CATEGORY_CHOICES, help_text="Selected service category")
    booking_date = models.DateField(help_text="Preferred service date")
    booking_time = models.TimeField(help_text="Preferred service time")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.customer_name} - {self.get_service_category_display()} on {self.booking_date}"
    
    class Meta:
        ordering = ['-created_at']  # Most recent first
        verbose_name = "Service Booking"
        verbose_name_plural = "Service Bookings"
