from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),  # Existing accounts endpoints
    path('', include('posts.urls')),     # Posts endpoints with api/ prefix
]
