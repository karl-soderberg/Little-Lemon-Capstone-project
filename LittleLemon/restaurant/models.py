from django.db import models


# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    no_of_guests = models.SmallIntegerField(default=1)

    def __str__(self): 
        return self.first_name


class Menu(models.Model):
    name = models.CharField(max_length=200) 
    price = models.IntegerField(null=False) 
    inventory = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name} : {str(self.price)}'

    def get_item(self):
        return f'{self.name} : {str(self.price)}'