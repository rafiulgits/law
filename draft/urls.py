from django.urls import path
from draft.views import ArticleView, AllArticles,DireactoryView, root_directories

urlpatterns = [
    path('article/', ArticleView.as_view()),
    path('article/all/', AllArticles.as_view()),
    path('directory/', DireactoryView.as_view()),
    path('root-directories/', root_directories)
]