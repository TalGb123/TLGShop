from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class HumanResources(models.Model):
    id = models.AutoField(primary_key=True)
    person_id = models.TextField(max_length=9)
    first_name = models.TextField()
    last_name = models.TextField()
    birth_date = models.DateTimeField()
    city = models.TextField()
    street = models.TextField()
    building_number = models.IntegerField()
    apartment_number = models.IntegerField()
    cellphone_number = models.TextField(max_length=10)
    # account = models.ForeignKey(User)
