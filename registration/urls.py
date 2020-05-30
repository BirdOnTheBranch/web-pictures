from django.urls import path
from .views import SignUpView, ProfileView, EmailUpdate, add_friend, delete_friend, get_friends

urlpatterns = [
    path('signup/', SignUpView.as_view(), name="signup" ),
    path('profile/', ProfileView.as_view(), name="profile" ),
    path('profile/email', EmailUpdate.as_view(), name="profile_email" ),
    path('addfriend/<username>', add_friend, name="add_friend"),
    path('deletefriend/<username>', delete_friend, name="delete_friend"),
    path('getfriends/<username>', get_friends, name="get_friends"),
]
