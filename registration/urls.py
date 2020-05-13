from django.urls import path
from .views import SignUpView, ProfileView, EmailUpdate

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup" ),
    path('profile/', ProfileView.as_view(), name="profile" ),
    path('profile/email', EmailUpdate.as_view(), name="profile_email" ),
]
