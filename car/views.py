import uuid

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View

from car.filter import CarFilter
from car.forms import CarForms


class CarsListView(View):
    def get(self, request):
        filter_class = CarFilter(request.GET, request=request)

        return render(
            request,
            'cars/list.html',
            {
                'extraContext': {
                    'title': 'Cars List'
                },
                'context': {
                    'situation': request.GET.get('situation'),
                    'title_of_page': request.GET.get('situation', '').upper(),
                    'filter': filter_class
                }
            }
        )


class CarsCreateView(View):
    def post(self, request):
        create_form = CarForms(request.POST, request.FILES)
        if create_form.is_valid():
            create_form.save()

            return redirect(
                f"{reverse('cars-list')}?situation={request.POST.get('situation')}"
            )

        return render(request, "cars/form.html", {
            "extraHeadContext": {
                "title": "Cars Create"
            },
            "context": {
                "situation": request.GET.get("situation"),
                "titleOfPage": request.GET.get("situation", "").upper(),
                "form": create_form
            }
        })

    def get(self, request):
        create_form = CarForms(
            initial={
                "car_id": str(uuid.uuid4())
            }
        )

        return render(request, "cars/form.html", {
            "extraHeadContext": {
                "title": "Cars Create"
            },
            "context": {
                "situation": request.GET.get("situation"),
                "titleOfPage": request.GET.get("situation", "").upper(),
                "form": create_form
            }
        })