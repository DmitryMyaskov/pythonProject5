from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    # address
    street = models.CharField(max_length=100)
    suite = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=100)
    # geo
    lat = models.DecimalField(decimal_places=4, max_digits=8)
    lng = models.DecimalField(decimal_places=4, max_digits=8)

    phone = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    # company
    compName = models.CharField(max_length=100, default="")
    compCatchPhrase = models.CharField(max_length=100)
    compBs = models.CharField(max_length=100)







class Post(models.Model):
    userId = models.IntegerField()
    id=models.IntegerField(primary_key=True)
    title=models.TextField()
    body=models.TextField()

