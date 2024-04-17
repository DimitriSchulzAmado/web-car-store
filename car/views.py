from django.shortcuts import render
from django.views.generic import View

from car.filter import CarFilter


class CarsListView(View):
    def get(self, request):
        filter_class = CarFilter(request.GET, request=request)

        return render(
            request,
            '',
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