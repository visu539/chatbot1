from django.urls import path
from .views import ProfileUpdateView, WhoAmIView

urlpatterns = [
    path("users/me/", WhoAmIView.as_view(), name="whoami"),
    path("users/me/profile/", ProfileUpdateView.as_view(), name="profile-update"),
]