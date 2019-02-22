from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.index, name ="home"),
    path('base/',views.base, name ="base"),
    path('about/',views.about, name ="about"),
]