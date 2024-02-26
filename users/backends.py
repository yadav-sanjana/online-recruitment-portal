from typing import Any
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models import QuerySet
from django.http import HttpRequest

UserModel = get_user_model()

class EmailBackend(ModelBackend):
    def authenticate(self, request, username, password: None) -> AbstractBaseUser | None:
        return super().authenticate(request, username, password)