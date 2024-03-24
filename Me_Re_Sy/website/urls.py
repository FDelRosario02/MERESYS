"""
URL configuration for Me_Re_Sy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from . import views
from django.urls import path

urlpatterns = [
    path('',views.home, name='home'),
    #path('',views.home, name='home'),
    path('logout/',views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('predict', views.predict, name ='predict'),
    path('patient/<int:pk>', views.patient_record, name='patient'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('update_patient/<int:pk>', views.update_patient, name='update_patient'),
    path('delete_patient/<int:pk>', views.delete_patient, name='delete_patient'),
    
]
