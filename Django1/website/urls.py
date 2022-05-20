from django.urls import path
from .views import home

urlpatterns = [
    path('', home),
    path('home/', home),
    # path('home/', home)
]