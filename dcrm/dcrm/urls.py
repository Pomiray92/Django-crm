
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("website.urls")),
    path("notification/", include("send_email.urls")),
    path("restapi/", include("app_restapi.urls"))
]
