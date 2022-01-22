"""Reserverest URL Configuration

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
from arsapp import views
from django.contrib.auth import views as auth
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('register/',views.register,name="register"),
    path('login/',views.Login, name="login"),
    path('ownerhome/',views.ownerhome,name="ownerhome"),
    path('userhome/',views.userhome,name="userhome"),
    path('reservation/',views.reservation,name="reservation"),
    path('logout/',views.logout,name="logout"),
    path('view_details/',views.reservation_list,name="view-details"),
    path('reservation_edit/<int:id>',views.reservation_edit,name="reservation_edit"),
    path('cancel-list/',views.cancel_list, name="cancel_list_url"),
    path('reservation_cancel/<int:id>',views.cancel_reservation, name="cancel_reservation_url"),

]

