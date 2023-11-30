from django.urls import path
from .views import keyword_extraction_view

app_name = 'symbol_detector'

urlpatterns = [
    path('extract-keywords/', keyword_extraction_view, name='extract_keywords'),
]
