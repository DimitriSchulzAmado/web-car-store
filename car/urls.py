from django.urls import path

from car.views import CarsListView

urlpatterns = [
    path('', CarsListView.as_view(), name='')
]