# models.py
from django.db import models
from django.contrib.auth.models import User

class UserQuery(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    query = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Query from {self.user.username}"

