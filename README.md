# AutoCare Services - Quick Setup Guide

## 1. Create Superuser
Run this command and follow the prompts:
```bash
.\venv\Scripts\python manage.py createsuperuser
```

## 2. Start Development Server
```bash
.\venv\Scripts\python manage.py runserver
```

## 3. Access the Application
- Homepage: http://127.0.0.1:8000/
- Admin Panel: http://127.0.0.1:8000/admin/

## 4. Add Sample Data via Admin
1. Login to admin panel with superuser credentials
2. Add Services (e.g., Car Wash, Oil Change, General Service)
3. Add Products (e.g., Engine Oil, Cleaning Kit)

## 5. Test the Application
- Create a new user account via Sign Up
- Login and access Services and Products pages
- Submit a contact form message
- Verify data in admin panel
