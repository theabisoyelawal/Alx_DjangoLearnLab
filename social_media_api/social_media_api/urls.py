from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),  # accounts endpoints
    path('api/posts/', include('posts.urls')),        # posts endpoints + feed
]
