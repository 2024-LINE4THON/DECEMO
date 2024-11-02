from django.contrib import admin
from django.urls import path, include
from account import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', account_views.index, name='index'),
    path('account/', include('account.urls')),
    path('question/', include('question.urls')),
]
