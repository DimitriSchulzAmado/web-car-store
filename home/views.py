from django.shortcuts import render
from django.views.generic import View  # CBV


class HomeView(View):
    def get(self, request):
        return render(
            request,
            'home.html',
            {
                "extraContext": {
                    "title": "Home",
                }
            }
        )
