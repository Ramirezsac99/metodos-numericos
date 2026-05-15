from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('taylor/', views.vista_taylor, name='taylor'),
    path('newton/', views.vista_newton, name='newton'),
    path('newton-mod/', views.vista_newton_mod, name='newton_mod'),
    path('secante/', views.vista_secante, name='secante'),
    path('biseccion/', views.vista_biseccion, name='biseccion'),
]