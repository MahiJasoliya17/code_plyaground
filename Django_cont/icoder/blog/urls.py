"""
URL configuration for icoder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from .import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.bloghome, name='bloghome'),
    path('<str:slug>', views.blogpost, name='blogpost'),
    path('handle-comment/', views.handle_comment, name='handle_comment'),  

]