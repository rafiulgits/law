"""law URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from graphene_django.views import GraphQLView
from law.graphql import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', include('account.urls')),
    path('api/blog/', include('blog.urls')),
    path('api/exam/', include('exam.urls')),
    path('api/draft/', include('draft.urls')),
    path('api/cpanel/', include('cpanel.urls'))
]

if settings.DEBUG:
    urlpatterns.append(path('api/graph', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))))