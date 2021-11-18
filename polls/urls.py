from django.urls import path

from polls.views import (
    AddPollUnitView,
    LGAListView,
    LGAPollUnitList,
    PollUnitDetailView,
    PollUnitListView,
)


urlpatterns = [
    path("", PollUnitListView.as_view(), name="index"),
    path("polls-unit/new/", AddPollUnitView.as_view(), name="polls-new"),
    path("polls-unit/list/", PollUnitListView.as_view(), name="polls-list"),
    path(
        "polls-unit/<str:unit_number>/details/",
        PollUnitDetailView.as_view(),
        name="polls-details",
    ),
    path("lga/list/", LGAListView.as_view(), name="lga-list"),
    path("lga/<str:lga_id>/details/", LGAPollUnitList.as_view(), name="lga-polls-list"),
]
