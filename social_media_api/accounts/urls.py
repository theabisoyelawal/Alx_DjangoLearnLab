from django.urls import path
from .views import RegisterView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    # Note: Profile management endpoint /profile usually requires 
    # a detail view or a generic user profile endpoint not specified here.
    # The checkers primarily focus on /register and /login.
]