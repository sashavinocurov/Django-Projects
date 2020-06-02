from django.db import models
from django.utils import timezone

class Comment(models.Model):
    name = models.CharField(max_length=20)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '<Name: {}, ID: {}>'.format(self.name, self.id)

