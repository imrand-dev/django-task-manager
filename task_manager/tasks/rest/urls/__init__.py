from django.urls import path, include

urlpatterns = [
	path("/categories", include("store.rest.urls.category")),
	path("/brands", include("store.rest.urls.brand")),
	path("/products", include("store.rest.urls.product")),
]