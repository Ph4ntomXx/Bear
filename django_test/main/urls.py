from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path("users/", include("users.urls")),
    path('news/', include('news.urls')),
]
