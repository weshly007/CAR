from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)  # Added resume field

    def __str__(self):
        return self.user.username

# from django.db import models

# # Create your models here.
# class UserModel(models.Model):
#     name = models.CharField(max_length=100)
#     age = models.IntegerField()
#     email = models.EmailField(max_length=100,unique=True)
#     password = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name