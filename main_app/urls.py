from django.urls import path
from .views import home, register, landing

urlpatterns = [
    path('', landing, name='landing'),
    path('home', home, name='landing'),
    path('register', register, name='register-landing')
    # Add more URL patterns as needed
]