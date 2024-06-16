from django.urls import include, path, re_path
from Authentication import views

urlpatterns = [
    path('Signup', views.SignUpApi),
    path('Login', views.LoginApi),
]
