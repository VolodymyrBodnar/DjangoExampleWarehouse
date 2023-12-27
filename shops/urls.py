from .views import list_shops
from django.urls import path


urlpatterns = [
    path('', list_shops),
]