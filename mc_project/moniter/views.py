from django.contrib.auth.decorators import login_required
from .models import patient
from .forms import PatientForm
import datetime
from django.utils import timezone
from django.shortcuts import render, redirect, reverse
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from user.models import emergency
from .serializers import EmergencySerializer


def CheckEmergency():
	e = emergency.objects.filter(state=1)
	em=EmergencySerializer(e,many=True)
	response_data={
        "success":True,
        "emergencies":em.data
    }
	return response_data

class ApiFirst(APIView):
    def get(self,request,format=None):
        response_data = CheckEmergency()
        return Response(response_data,status=status.HTTP_200_OK)

# Create your views here.
@login_required()
def index(request):
	context={}
	return render(request , 'moniter/index.html',context)

@login_required()
def home(request):
	context={}
	print("#######home")
	patients = patient.objects.all()
	print(patients)
	context['patients']=patients
	return render(request , 'moniter/home.html',context)

@login_required()
def addpatient(request):
	context={}
	if request.method=='POST':
		print("$$$$$$$$$post")
		form=PatientForm(request.POST)
		if form.is_valid():
			form.save(commit =True)
		return redirect('addpatient')	
	context['patientform'] = PatientForm(request.POST)
	print("#######addpatient")
	patients = patient.objects.all()
	print(patients)
	context['patients']=patients
	return render(request , 'moniter/addpatient.html',context)
