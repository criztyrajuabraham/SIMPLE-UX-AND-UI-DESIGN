from django.urls import path

from testapp import views

urlpatterns = [

    path("", views.home, name="home"),
    path("login",views.login,name="login"),
    path("register",views.register,name="register"),
    path("enquiry",views.enquiry,name="enquiry"),
    path("logout",views.logout,name="logout"),
    path("details",views.details,name="details"),

]
