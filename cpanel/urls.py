from django.urls import path
from cpanel.views import Dashboard

urlpatterns = [
    path('dash/', Dashboard.as_view())
]