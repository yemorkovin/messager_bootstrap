from django.urls import path
from .views import *
urlpatterns = [
    path('', index),
    path('lk', lk),
    path('ajaxReg', ajaxReg),
    path('ajaxAuth', ajaxAuth),
    path('logout', logout)
]