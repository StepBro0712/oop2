from django.contrib import admin
from django.contrib.auth.views import LoginView

# Register your models here.
from .models import AdvUser

admin.site.register(AdvUser)


class BBLoginView(LoginView):
    template_name = 'main/login.html'
