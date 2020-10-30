"""simplesocial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path
from conversations import views

app_name = 'conversations'

urlpatterns = [
    re_path('^start_new/(?P<recipent_pk>\d+)/$', views.start_new_conversation_from_profile, name='start_new'),
    re_path('^conv_page/(?P<conversation_pk>\d+)/$', views.conversation_view, name='conversation_page'),
    path('convs_panel/', views.conversations_panel, name='conversations_panel'),
]
