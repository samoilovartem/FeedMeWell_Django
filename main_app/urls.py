from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    # path('found_restaurants/', show_found_restaurants, name='found_restaurants'),
]

