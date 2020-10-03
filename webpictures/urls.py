"""webpictures URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from pages.urls import pages_patterns
from profiles.urls import profiles_patterns
from messenger.urls import messenger_patterns
from likes.urls import likes_patterns
from contact.urls import contact_patterns
from actions.urls import actions_patterns
from django.contrib.auth import views as auth_views

import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    # Django-debug-toolbar
    path('__debug__/', include(debug_toolbar.urls)),
    path('pages/', include(pages_patterns, namespace='pages')),
    # path auth
    path('accounts/', include('django.contrib.auth.urls')),
    # django-social-auth
    path('social-auth/', include('social_django.urls', namespace='social')),
    # path register
    path('accounts/', include('registration.urls')),
    path('profiles/', include(profiles_patterns)),
    path('messenger/', include(messenger_patterns)),
    path('likes/', include(likes_patterns)),
    path('friends/', include(contact_patterns)),
    path('actions/', include(actions_patterns)),
]


# Logic whit server media files in debug mode
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
