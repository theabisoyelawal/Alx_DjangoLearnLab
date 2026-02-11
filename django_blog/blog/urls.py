from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='blog-home'),
    path('search/', views.search_posts, name='post-search'),
    path('tags/<str:tag_name>/', views.posts_by_tag, name='posts-by-tag'),
    # Existing CRUD URLs here
    # Example:
    # path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    # path('post/new/', views.PostCreateView.as_view(), name='post-create'),
    # path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post-update'),
    # path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
]
