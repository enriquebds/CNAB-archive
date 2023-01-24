from django.urls import path
from .views import upload

urlpatterns = [
    path("cnab/", upload, name='cnab')
]