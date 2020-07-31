from django.urls import path

from . import views

urlpatterns = [
    path('', views.empty, name='empty'),
    path('index', views.index, name='index'),
    path('index/<str:subarticle>', views.index, name='index'),
    path('about', views.about, name='about'),
    path('about/<str:subarticle>', views.about, name='about'),
    path('vision', views.vision, name='vision'),
    path('getlockzy', views.getlockzy, name='getlockzy'),
    path('getlockzy/<str:subarticle>', views.getlockzy, name='getlockzy'),
]
