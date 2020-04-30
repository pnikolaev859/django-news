from django.urls import path
from articles.views import ArticlesListView, detail, about


urlpatterns = [
    path('', ArticlesListView.as_view(), name='all_news'),
    path('<int:id>/', detail, name='news_detail'),
    path('about/', about)
]
