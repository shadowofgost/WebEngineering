"""
# @Author           : Albert Wang
# @Copyright Notice : Copyright (c) 2022 Albert Wang 王子睿, All Rights Reserved.
# @Time             : 2022-01-13 01:42:51
# @Description      :
# @Email            : shadowofgost@outlook.com
# @FilePath         : /WebEngineering/WebEngineering/urls.py
# @LastAuthor       : Albert Wang
# @LastTime         : 2022-03-10 20:14:00
# @Software         : Vscode
"""
"""WebEngineering URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="WebEngineering",
        default_version="v1.0",
        description="WebEngineering API and documentation",
        terms_of_service="https://www.cnblogs.com/jinjiangongzuoshi/",
        contact=openapi.Contact(email="shadowofgost@outlook.com"),
        license=openapi.License(name="shadowofgost"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path("admin/", admin.site.urls),
    # 配置django-rest-framwork API路由
    # path('api/', include('api.urls')),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    # 配置drf-yasg路由
    re_path(
        "^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "doc/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path("polls/", include("polls.urls")),
    ##path('captcha/', include('captcha.urls')),
]
