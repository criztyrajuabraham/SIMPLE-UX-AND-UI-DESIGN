

from django.db import models



class Details(models.Model):

    username = models.CharField(max_length=250)
    dateofbirth = models.DateField(null=True, blank=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=20,default=False)
    phone = models.IntegerField(unique=True)
    mail = models.EmailField(max_length=100)
    comments = models.TextField(max_length=256)
    parent_selection = models.CharField(max_length=20)
    child_selection = models.CharField(max_length=20)
    user_interest = models.CharField(max_length=20)

    def __str__(self):
        return self.username


