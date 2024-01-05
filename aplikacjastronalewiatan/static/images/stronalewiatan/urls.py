"""
URL configuration for stronalewiatan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, include
from aplikacjastronalewiatan import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Pusta ścieżka '' oznacza stronę główną
    # Tutaj możesz dodać więcej ścieżek do innych widoków

    #path('aplikacjastronalewiatan/', include('aplikacjastronalewiatan.urls')),  # Dołączanie ścieżek z aplikacji
    path('o_nas/',views.o_nas, name='o_nas'),
    path('kontakt/', views.kontakt, name='kontakt'),
    path('usługi/',views.usługi, name='usługi'),
]
