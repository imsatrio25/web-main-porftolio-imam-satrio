from django.urls import path
from .views import index, second

urlpatterns = [
    path('', index, name='home'),
    path('port1/', second, name='second')
]