from django.urls import path
from . import views

# App-level URL patterns
urlpatterns = [
    # Public routes
    path('', views.home_view, name='home'),  # Homepage
    path('signup/', views.signup_view, name='signup'),  # Sign Up page
    path('signin/', views.signin_view, name='signin'),  # Sign In page
    path('logout/', views.logout_view, name='logout'),  # Logout action
    path('car-wash-booking/', views.car_wash_booking_view, name='car_wash_booking'),  # Car Wash Booking
    
    # Protected routes (require authentication)
    path('services/', views.services_view, name='services'),  # Services listing and booking
]
