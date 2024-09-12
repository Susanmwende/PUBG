# pubg_clone/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('game.urls')),  # Include the game app URLs
    path('', TemplateView.as_view(template_name="index.html")),  # Serve the index.html
]