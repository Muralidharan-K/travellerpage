from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    desc = models.TextField()
    offer = models.BooleanField()