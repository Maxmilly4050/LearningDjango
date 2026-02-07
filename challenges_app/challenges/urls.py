from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("<int:number>",views.challenge_by_number),
    path("<str:month>", views.challenge_by_month, name="challenges")
]