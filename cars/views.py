from django.shortcuts import render
from django.http import JsonResponse
from .models import *
# Create your views here.
def listCars(request):
    cars=Car.objects.all()
    cars_json=[]
    for car in cars:
        print(car.car_model)
        cars_json.append({"car_model":car.car_model,"door_num":car.door_no,"seats":car.seat_no,"desc":car.description,"year_of_manu":car.year_of_man,"class":car.car_class,"image":"http://localhost:8080/carpics/2.jpg"})
    return JsonResponse({"state":"ok","cars":cars_json})