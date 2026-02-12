from django.urls import path
from . import views
from .views import PostByTagListView

urlpatterns = [
    # -----------------------------
    # Authentication URLs (Task 2)
    # -----------------------------
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),

    # -----------------------------
    # Post CRUD URLs (Task 3)
    # -----------------------------
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

    # -----------------------------
    # Comment URLs (Task 4)
    # -----------------------------
    path('post/<int:pk>/comments/new/', views.CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', views.CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),

    # -----------------------------
    # Tag URLs (Task 5)
    # -----------------------------
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name='posts_by_tag'),

    # -----------------------------
    # Search URL (Task 5)
    # -----------------------------
    path('search/', views.search_posts, name='search_posts'),
]
