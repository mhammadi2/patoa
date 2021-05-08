from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import jsonfield
from django.conf import settings
from .validators import validate_patnof
from django import forms


class Patent(models.Model):
    # def validate_patnof(value):
    #         if len(value) !=8 and  len(value) !=11:
    #             raise  ValidationError("Need to be 8 or 11 in length")
    #         else:
    #             return value

    # patnof = models.CharField(max_length=11,  validators=[validate_patnof], null=True)
    patnof = models.IntegerField(null=True, validators=[validate_patnof])
    claim_list = models.JSONField(null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    #user = models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
    

    def __str__(self):
        return self.user.username


   