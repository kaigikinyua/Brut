from django.urls import path
from . import views
urlpatterns = [
    path('listCars',views.listCars,name="listCars")
]
