from django.contrib import admin
from .models import Patient  # Ensure the correct model is imported

admin.site.register(Patient)  # Ensure the model is registered
