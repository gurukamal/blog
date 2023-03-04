from django.urls import path, include
from .views import IncidentList
urlpatterns = [
    path("get-details/",IncidentList.as_view(),name="details"),
    # path("post-details",IncidentDetail.as_view())

    ]