from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('o_nas/', views.o_nas, name='o_nas'),
    path('kontakt/', views.kontakt, name='kontakt'),
    path('usługi/', views.usługi, name='usługi')
]

