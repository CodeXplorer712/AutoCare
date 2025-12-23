from django.urls import path
from . import views

# App-level URL patterns
urlpatterns = [
    # Public routes
    path('', views.home_view, name='home'),  # Homepage
    path('signup/', views.signup_view, name='signup'),  # Sign Up page
    path('signin/', views.signin_view, name='signin'),  # Sign In page
    path('logout/', views.logout_view, name='logout'),  # Logout action
    path('contact/', views.contact_view, name='contact'),  # Contact page
    
    # Protected routes (require authentication)
    path('services/', views.services_view, name='services'),  # Services listing
    path('products/', views.products_view, name='products'),  # Products listing
]
