from django.db import models
import jsonfield

# Create your models here.
class InfoModel(models.Model):
    rollnumber=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.EmailField()
    phone=models.IntegerField()
    extra_data = jsonfield.JSONField()
    