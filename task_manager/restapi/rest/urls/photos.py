from django.urls import path

from restapi.rest.views.photos import PrivatePhotoView, PrivatePhotoDetailView

urlpatterns = [
    path("/<uuid:photo_uid>", PrivatePhotoDetailView.as_view(), name="photo-detail"),
    path("", PrivatePhotoView.as_view(), name="photo-list"),
]