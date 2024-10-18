from django.shortcuts import render, redirect
from .models import Patient
import random

def landing_page(request):
    return render(request, 'patients/landing.html')

# Patient Registration View
def register_patient(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        illness = request.POST['illness']
        address = request.POST['address']
        patient_id = random.randint(1000000000, 9999999999)  # Generate random 10-digit ID
        
        # Save patient
        Patient.objects.create(name=name, age=age, illness=illness, address=address, patient_id=patient_id, status='Admitted')
        return redirect('patient_success', patient_id=patient_id)
    return render(request, 'patients/register.html')

# Patient Search View
def search_patient(request):
    if request.method == 'POST':
        patient_id = request.POST['patient_id']
        patient = Patient.objects.filter(patient_id=patient_id).first()
        return render(request, 'patients/details.html', {'patient': patient})
    return render(request, 'patients/search.html')

# View All Patients
def view_patients(request):
    patients = Patient.objects.all()
    return render(request, 'patients/list.html', {'patients': patients})

# Success Page
def success(request, patient_id):
    return render(request, 'patients/success.html', {'patient_id': patient_id})
