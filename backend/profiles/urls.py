from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import profile_detail, profiles_list

urlpatterns = [

    path('', profiles_list),
    path('<int:pk>/', profile_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)
