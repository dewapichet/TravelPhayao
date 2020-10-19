from django.db import models

# Create your models here.

class Amphoe(models.Model):
    Amphoe_name  = models.CharField(max_length=70)

    def __str__(self):
        return f'Amphoe :{self.Amphoe_name}'

class Place(models.Model):

    Place_name = models.CharField(max_length=70)
    Place_content = models.TextField()
    Amphoe = models.ForeignKey(Amphoe, on_delete=models.CASCADE)


    def __str__(self):
        return f'Amphoe :{self.Amphoe.Amphoe_name}, Place : {self.Place_name}'
