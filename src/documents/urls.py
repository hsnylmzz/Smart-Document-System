from django.urls import path
from documents.views import *

urlpatterns = [
    path('', index, name='AnaSayfa'),
]
