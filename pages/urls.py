from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('favorites/', views.favorite_posts, name='favorites'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('<slug:slug>/add_favorite/',
         views.add_favorite, name='add_favorite'),
    path('<slug:slug>/remove_favorite/',
         views.remove_favorite, name='remove_favorite'),
]
