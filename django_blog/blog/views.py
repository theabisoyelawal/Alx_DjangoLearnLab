from django.views.generic import ListView
from .models import Post  # Make sure you have a Post model in models.py

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'  # Make sure this template exists
    context_object_name = 'posts'          # Used in the template as {{ posts }}
