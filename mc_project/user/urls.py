from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('api',views.ApiFirst.as_view(),name="ApiFirst"),
]
