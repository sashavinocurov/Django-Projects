from django.db import models
import re
import requests 
from datetime import datetime
# import bcrypt

class TvshowManager(models.Manager):
    def newshow_validate(self, formData):
        release_date= datetime.strptime(formData['release_date'], '%Y-%m-%d')
        errors = {}
        if len(formData["title"]) < 3:
            errors["title"] = "Not enough characters in title"
        if len(formData["network"]) < 2:
            errors["network"] = "Not enough characters in network"
        if release_date >= datetime.now():
            errors["release_date"]= "Invalid Date"
        if len(formData["description"]) < 10 or len(formData["description"] !=0):
            errors["description"] = "Not enough characters in description"
        return errors


class Tvshow(models.Model):
    title= models.CharField(max_length=255)
    network= models.CharField(max_length=15)
    release_date= models.DateField()
    description= models.TextField(null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects= TvshowManager()


# class IMDB_Fetcher(models.Model):
    
