from django.db import models

# Create your models here.
class Car(models.Model):
    car_model=models.CharField(max_length=50)
    car_class=models.CharField(default="Saloon", max_length=50)
    year_of_man=models.CharField(max_length=50)
    seat_no=models.IntegerField(default=4)
    door_no=models.IntegerField(default=4)
    description=models.CharField(max_length=200)
    avg_rating=models.IntegerField(default=0)
    def __str__(self):
        return self.car_model
    

class CarPhoto(models.Model):
    car=models.ForeignKey("cars.Car", verbose_name=("car_model"), on_delete=models.CASCADE)
    pic_path=models.CharField(max_length=1000)

class CarRating(models.Model):
    car=models.ForeignKey("cars.Car", verbose_name=("car_model"), on_delete=models.CASCADE)
    stars=models.IntegerField()