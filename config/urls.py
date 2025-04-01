"""djangodocker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add, include('main.urls')),
    url(r'^admin/', admin.site.urls),
]"""
import types
from django.conf import settings
from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from .admin import get_app_list
from drf_spectacular.views import (
    SpectacularSwaggerView,
    SpectacularAPIView,
    SpectacularRedocView,
)

admin.site.get_app_list = types.MethodType(get_app_list, admin.site)

urlpatterns = [
    # YOUR PATTERNS
    path(
        r"{}api/schema/".format(settings.URI_PREFIX),
        SpectacularAPIView.as_view(),
        name="schema",
    ),
    # Optional UI:
    path(
        r"{}api/schema/swagger-ui/".format(settings.URI_PREFIX),
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        r"{}api/schema/redoc/".format(settings.URI_PREFIX),
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]

urlpatterns += [
    url(r"^{}".format(settings.URI_PREFIX), include("solid_backend.urls")),
    url(r"^{}".format(settings.URI_PREFIX), include("solid_backend.media_object.urls")),
    url(r"^{}admin/".format(settings.URI_PREFIX), admin.site.urls),
]
