from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

from .forms import RegisterForm


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'users/authentication/register.html'
    success_url = reverse_lazy('login')


class CustomLoginView(LoginView):
    template_name = 'users/authentication/login.html'


class CustomLogoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse('home'))


''''
universal_drf_template
minio
redis
mongodb
mysql
postgres
celery
sms(eskiz)
click, payme, uzum
elasticsearch
graphql
websocket
github, gitlab (cicd)
docker compose
'''
