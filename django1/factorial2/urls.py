from django.urls import path
from factorial2.views import home
urlpatterns = [path('', home),]