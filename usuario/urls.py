from django.urls import path
from . import views 

urlpatterns = [
    path('usuarios/', views.usuario_list),
    path('usuario/<str:login>/', views.usuario_detail)
]