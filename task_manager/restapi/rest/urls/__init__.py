from django.urls import path, include

urlpatterns = [
    path("/tasks", include("restapi.rest.urls.tasks")),
    path("/photos", include("restapi.rest.urls.photos")),
]