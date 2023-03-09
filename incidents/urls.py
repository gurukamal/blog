from django.urls import path, include
from .views import IncidentList
urlpatterns = [
    path("details/",IncidentList.as_view(),name="details"),

    ]