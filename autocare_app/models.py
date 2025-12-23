from django.db import models

# Service Model - Represents car services offered (e.g., Car Wash, Oil Change)
class Service(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the service")
    description = models.TextField(help_text="Detailed description of the service")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price in currency")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


# Product Model - Represents car-related products (e.g., Engine Oil, Cleaning Kit)
class Product(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the product")
    description = models.TextField(help_text="Detailed description of the product")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Price in currency")
    image_placeholder = models.CharField(max_length=200, default="https://via.placeholder.com/300", help_text="Image URL placeholder")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']


# ContactMessage Model - Stores contact form submissions
class ContactMessage(models.Model):
    name = models.CharField(max_length=100, help_text="Sender's name")
    email = models.EmailField(help_text="Sender's email address")
    message = models.TextField(help_text="Message content")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message from {self.name} - {self.created_at.strftime('%Y-%m-%d')}"
    
    class Meta:
        ordering = ['-created_at']  # Most recent first

