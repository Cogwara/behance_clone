# urls.py in your project's main directory

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Include accounts app URLs
    # path('projects/', include('projects.urls')),  # Include projects app URLs
    # Add other app URLs here
]
