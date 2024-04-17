import django_filters
from django import forms

from car.models import Car


class CarFilter(django_filters.FilterSet):
    model = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(
            attrs={
                'class': 'bg-app-gray-400 rounded-none px-3 placeholder:font-semibold placeholder:font-roboto '
                         'placeholder:text-app-blue-300 py-1 placeholder:text-sm',
                'placeholder': 'INPUT THE MODEL'
            }
        )
    )
    brand = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(
            attrs={
                'class': 'bg-app-gray-400 rounded-none px-3 placeholder:font-semibold placeholder:font-roboto '
                         'placeholder:text-app-blue-300 py-1 placeholder:text-sm',
                'placeholder': 'INPUT THE BRAND'
            }
        )
    )
    car_year = django_filters.NumberFilter(
        lookup_expr='icontains',
        widget=forms.NumberInput(
            attrs={
                'class': 'bg-app-gray-400 rounded-none px-3 placeholder:font-semibold placeholder:font-roboto '
                         'placeholder:text-app-blue-300 py-1 placeholder:text-sm',
                'placeholder': 'INPUT THE YEAR'
            }
        )
    )
    situation = django_filters.CharFilter(
        lookup_expr='exact',
        widget=forms.TextInput(
            attrs={
                'class': 'bg-app-gray-400 rounded-none px-3 placeholder:font-semibold placeholder:font-roboto '
                         'placeholder:text-app-blue-300 py-1 placeholder:text-sm hidden',
                'placeholder': 'INPUT THE BRAND'
            }
        )
    )

    class Meta:
        model = Car
        fields = ['model', 'brand', 'car_year']