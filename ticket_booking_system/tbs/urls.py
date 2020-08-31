"""ticket_booking_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from django.urls import path
from .views import Ticket_List,submit,Person_List,\
    Ticket_filter,Movie_List,Movie_details,\
    Person_details,Ticket_details
urlpatterns = [
    path('ticket/',Ticket_List),
    path('person/',Person_List),
    path('movie/',Movie_List),
    path('ticket/<int:pk>/',Ticket_details),
    path('person/<int:pk>/',Person_details),
    path('movie/<int:pk>/',Movie_details),
    path('ticket_filter/<int:pk>/',Ticket_filter)
    #path('',submit)
]
