
from django.urls import path
from .views import signup, login, profile,logout

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('profile/',profile,name='profile'),
    path('success/', profile, name='success'),
    path('logout/', logout, name='logout'),
]