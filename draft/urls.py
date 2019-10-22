from django.urls import path
from draft.views import Article

urlpatterns = [
    path('/', Article.as_view()),
]