from django.urls import path
from .views import signup, login, logout, index, home, check_username, toggle_bgm, test

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('home/', home, name='home'),
    path('check-username/', check_username, name='check_username'),
    path('toggle-bgm/', toggle_bgm, name='toggle_bgm'),
    path('test/', test, name='test'),
]