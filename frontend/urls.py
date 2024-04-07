from django.urls import path
from . import views


app_name = "frontend"

urlpatterns = [
    path("", views.index, name="index"),
    path("news/", views.news, name="news"),
    path("contact/", views.contact, name="contact"),
    path("login/", views.user_login, name="login"),
    
]