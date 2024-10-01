from django.urls import path
from . import views

urlpatterns = [
    path('encode/', views.encode_payload, name='encode_payload'),
    path('decode/', views.decode_payload, name='decode_payload'),
]
