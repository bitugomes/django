from django.urls import path
from meus_games.views import inicio

urlpatterns = [

    path('', inicio),
]
