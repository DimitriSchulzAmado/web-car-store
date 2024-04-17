from django.db import models

import uuid


class Car(models.Model):
    FUEL_TYPE_CHOICES = (
        ('GASOLINE', 'Gasoline'),
        ('ALCHOHOL', 'Alcool'),
        ('DIESEL', 'Diesel')
    )

    CAR_TYPE_CHOICES = (
        ('AUTOMATIC', 'Automatico'),
        ('MANUAL', 'Manual')
    )

    car_id = models.UUIDField(
        primary_key=True,
        auto_created=True,
        default=str(uuid.uuid4()),
        editable=False
    )
    brand = models.CharField(max_length=100)
    car_year = models.IntegerField()
    color = models.CharField(max_length=10)
    description = models.TextField(max_length=1024)
    motor_detail = models.CharField(max_length=1024)
    fuel = models.CharField(max_length=10, choices=FUEL_TYPE_CHOICES)
    kilometers = models.DecimalField(decimal_places=2, max_digits=10)
    version = models.CharField(max_length=24)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    model = models.CharField(max_length=20, default='new')
    car_type = models.CharField(max_length=10, choices=CAR_TYPE_CHOICES)

    situation = models.CharField(max_length=10, default='new')

    photo_car = models.ImageField(upload_to='photos/', blank=True)

    def to_dict(self):
        return {
            'car_id': str(self.car_id),
            'brand': self.brand,
            'car_year': self.car_year,
            'color': self.color,
            'description': self.description,
            'motor_detail': self.motor_detail,
            'fuel': self.fuel,
            'kilometers': self.kilometers,
            'version': self.version,
            'price': self.price,
            'model': self.model,
            'car_type': self.car_type,
            'situation': self.situation,
            'photo_car': self.photo_car.url
        }

    def __str__(self):
        return f'Car:  {self.car_id}'
