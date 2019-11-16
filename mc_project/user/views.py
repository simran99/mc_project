
import datetime
from django.utils import timezone
from django.shortcuts import render

from django.shortcuts import render, redirect, reverse
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.response import Response
from .models import emergency
from moniter.models import patient

def AddEmergency(pid):
	e = emergency(pid=patient.objects.get(pid=pid),state=1,timestamp=datetime.datetime.now())
	e.save()
	response_data={
        "success":True,
        "message":"Success"
    }
	return response_data

class ApiFirst(APIView):
    def get(self,request,format=None):
        params= request.query_params
        response_data = AddEmergency(params['pid'])
        return Response(response_data,status=status.HTTP_200_OK)