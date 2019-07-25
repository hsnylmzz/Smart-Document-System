from django.urls import path

from documents.views import home, file


urlpatterns = [
    path('', home, name='home'),
    path('file/', file, name='upload files'),
    ]
