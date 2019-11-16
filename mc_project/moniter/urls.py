from django.urls import path
from django.conf.urls import url, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home' , views.home , name='home'),
    path('addpatient' , views.addpatient , name='addpatient'),
    url('checkemergency',views.ApiFirst.as_view(),name="ApiFirst"),
]