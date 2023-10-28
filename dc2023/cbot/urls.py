from .views import *
from django.urls import path
urlpatterns = [
    path('chat', testview.as_view(), name='main'),
]
