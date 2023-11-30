from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    # Include the symbol_detector app URLs
    path('symbol-detector/', include('symbol_detector.urls', namespace='symbol_detector')),
]