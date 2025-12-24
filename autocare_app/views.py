from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm
from .models import CarWashBooking, ServiceBooking


# ==================== PUBLIC VIEWS ====================

# Home View - Display homepage with hero section and CTAs
def home_view(request):
    """
    Homepage view accessible to all users.
    Displays hero section, brief description, and call-to-action buttons.
    """
    return render(request, 'home.html')


# Sign Up View - User registration
def signup_view(request):
    """
    Handle user registration.
    GET: Display signup form
    POST: Process form submission and create new user
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Auto-login after successful registration
            messages.success(request, f'Welcome {user.username}! Your account has been created.')
            return redirect('home')  # Redirect to homepage
    else:
        form = SignUpForm()
    
    return render(request, 'signin.html', {'form': form, 'show_signup': True})


# Sign In View - User login
def signin_view(request):
    """
    Handle user login.
    GET: Display login form
    POST: Authenticate user credentials
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            # Redirect to 'next' parameter or homepage
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'signin.html')


# Logout View - User logout
def logout_view(request):
    """
    Handle user logout and redirect to homepage.
    """
    logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('home')


# Car Wash Booking View - Display car wash booking page
def car_wash_booking_view(request):
    """
    Display car wash booking page.
    GET: Display booking form with package options
    POST: Handle booking form submission and save to database
    """
    if request.method == 'POST':
        # Get form data
        customer_name = request.POST.get('customer_name')
        phone = request.POST.get('phone')
        car_number = request.POST.get('car_number')
        address = request.POST.get('address')
        wash_package = request.POST.get('wash_package')
        booking_date = request.POST.get('booking_date')
        booking_time = request.POST.get('booking_time')
        
        # Create and save booking to database
        booking = CarWashBooking.objects.create(
            customer_name=customer_name,
            phone=phone,
            car_number=car_number,
            address=address,
            wash_package=wash_package,
            booking_date=booking_date,
            booking_time=booking_time
        )
        
        # Show success message
        messages.success(request, f'Booking confirmed for {customer_name}! We will contact you shortly.')
        return redirect('car_wash_booking')
    
    return render(request, 'carwash.html')


# ==================== PROTECTED VIEWS (Login Required) ====================

# Services View - Display all available services
@login_required
def services_view(request):
    """
    Display all car services and handle service booking submissions.
    Requires user to be logged in.
    GET: Display services page
    POST: Handle booking form submission
    """
    if request.method == 'POST':
        # Get form data
        customer_name = request.POST.get('customer_name')
        phone = request.POST.get('phone')
        car_number = request.POST.get('car_number')
        address = request.POST.get('address')
        service_category = request.POST.get('service_category')
        booking_date = request.POST.get('booking_date')
        booking_time = request.POST.get('booking_time')
        
        # Create and save booking to database
        booking = ServiceBooking.objects.create(
            customer_name=customer_name,
            phone=phone,
            car_number=car_number,
            address=address,
            service_category=service_category,
            booking_date=booking_date,
            booking_time=booking_time
        )
        
        # Show success message
        messages.success(request, f'Service booking confirmed for {customer_name}! We will contact you shortly.')
        return redirect('services')
    
    return render(request, 'services.html')

