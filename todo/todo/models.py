from django.db import models
from django.contrib.auth.models import User

class TODOO(models.Model):from django.db import models
from django.contrib.auth.models import User

class TODOO(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)  # needed for ordering

    
    def __str__(self):
        return self.title
