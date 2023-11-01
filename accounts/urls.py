from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.shortcuts import redirect
from django.urls import path
from .views import *


def redirecionar(request):
    return redirect('user-list')


urlpatterns = [
    path("login/", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

    path('users/', UserListView.as_view(), name='user-list'),
    path('user/create/', UserCreateView.as_view(), name='user-create'),
    path('user/update/<int:pk>/', PasswordChangeView.as_view(template_name="user_form.html"), name='user-update'),
    path('password_change/done/', redirecionar, name='password_change_done'),
    path('user/delete/<int:pk>/', UserDeleteView.as_view(), name='user-delete'),
]
