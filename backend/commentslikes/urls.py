
from django.urls import path
from rest_framework import urlpatterns 

from rest_framework.urlpatterns import format_suffix_patterns
from .views import commentslikes_list, commentslike_detail

urlpatterns = [
    path('', commentslikes_list),
    pat('<int:pk>/', commentslike_detail ),
]

urlpatterns = format_suffix_patterns(urlpatterns)