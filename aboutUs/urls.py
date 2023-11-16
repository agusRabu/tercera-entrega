from django.urls import path
from aboutUs.views import aboutUs

urlpatterns = [
        path('', aboutUs, name="aboutUs"),
]