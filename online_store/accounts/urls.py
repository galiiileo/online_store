from django.urls import path, include

from .views import profile_view, registerView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [


    path("",include('django.contrib.auth.urls')),

    path("profile/",profile_view,name="profile"),
    path("signup/",registerView.as_view(),name="signup"),



]