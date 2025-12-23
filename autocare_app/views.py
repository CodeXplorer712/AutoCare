from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, ContactForm
from .models import Service, Product


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
    
    return render(request, 'signup.html', {'form': form})


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


# Contact View - Display and handle contact form
def contact_view(request):
    """
    Display contact form and handle submissions.
    Form data is saved to the database (no email sending).
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Save contact message to database
            messages.success(request, 'Thank you! Your message has been sent successfully.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})


# ==================== PROTECTED VIEWS (Login Required) ====================

# Services View - Display all available services
@login_required
def services_view(request):
    """
    Display all car services.
    Requires user to be logged in.
    """
    services = Service.objects.all()  # Get all services from database
    return render(request, 'services.html', {'services': services})


# Products View - Display all available products
@login_required
def products_view(request):
    """
    Display all car-related products.
    Requires user to be logged in.
    """
    products = Product.objects.all()  # Get all products from database
    return render(request, 'products.html', {'products': products})

