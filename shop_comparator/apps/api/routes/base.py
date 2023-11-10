from django.contrib import admin
from django.urls import path
from ninja_extra import NinjaExtraAPI

api = NinjaExtraAPI()

# api.add_router("/", product_router)

urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/", api.urls),
]
