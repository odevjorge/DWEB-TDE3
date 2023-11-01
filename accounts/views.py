# Em seu arquivo views.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'password1', 'password2']


class UserCreateView(CreateView):
    model = User
    template_name = 'user_form.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('user-list')


@method_decorator(login_required, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    template_name = 'user_confirm_delete.html'
    success_url = reverse_lazy('user-list')
