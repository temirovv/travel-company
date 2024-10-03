from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField

User = get_user_model()


class RegisterForm(UserCreationForm):
    email = EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user





# Create your views here.
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
