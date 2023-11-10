from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

print(static(settings.STATIC_URL, document_root=settings.STATIC_ROOT))

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.core.urls")),
    path("", include("apps.api.routes")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
