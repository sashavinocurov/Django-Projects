from django.db import models
import re
from datetime import datetime
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def user_validate(self, formData): 
        dob= datetime.strptime(formData['dob'], '%Y-%m-%d')
        errors ={}
        if len(formData["first_name"]) < 2:
            errors["first_name"] = "Characters enough not first name"
        if len(formData["last_name"]) < 2:
            errors["last_name"] = "Characters enough not last name"
        if not EMAIL_REGEX.match(formData["email"]):
            errors["email"] = "Invalid address email not"
        if User.objects.filter(email=formData["email"]):
            errors["email"] = "This email already exist"
        if dob >= datetime.now():
            errors["dob"] = "Child of the future, FBI heading your way"
        if formData["password"] != formData ["confirm"]:
            errors["pasword"] = "Match not Passwords"
        return errors 
    def login_validate(self, formData):
        errors = {}
        my_user = User.objects.filter(email=formData["email"])
        if not my_user:
            errors["email"] = "Email exit not"
        if not EMAIL_REGEX.match(formData["email"]):
            errors["email"] = "Invalid address email not"
        else: 
            my_user = my_user [0]
            if not bcrypt.checkpw(formData['password'].encode(), my_user.password.encode()):
                errors['password'] = "Incorrect password is not"
        return errors

class User(models.Model):
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    email= models.CharField(max_length=255)
    dob= models.DateField(null=True)
    password= models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects= UserManager()

