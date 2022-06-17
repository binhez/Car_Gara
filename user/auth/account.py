from django.contrib.auth import authenticate
from django.contrib.auth.models import User


def _login(username, password):
    user = authenticate(username=username, password=password)
    return user


def _signup(username, email, password):
    check_user = User.objects.filter(username=username)
    if len(check_user) > 0:
        return False
    else:
        newuser = User.objects.create_user(username=username, email=email, password=password)
        newuser.save()
        return True
