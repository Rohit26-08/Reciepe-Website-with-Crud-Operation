"""
URL configuration for recipe project.

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
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import index,registration,update,insert,delete,login_page,logout_page

urlpatterns = [

    path('',index,name='home'),
    path('registration/',registration,name='regitration'),
       path('insert/',insert,name='insert'),
          path('update/<id>/',update,name='update'),
          path('delete/<id>/',delete,name='delete'),
                    path('login/',login_page,name='login'),
                       path('logout/',logout_page,name='logout'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
