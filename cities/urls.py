from django.urls import path

from .views import *
from .views import CityDetailView

urlpatterns = [
    path('', home, name='home'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
]