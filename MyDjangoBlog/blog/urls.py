# blog/urls.py
from django.urls import path

from .views import BlogListView, BlogDetailView, AddLike # нові зміни

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'), # нові зміни
    path('', BlogListView.as_view(), name='home'),
    path('<int:pk>/add_like/', view=AddLike.as_view(), name="add_like")
]
