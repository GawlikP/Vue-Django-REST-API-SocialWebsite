from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from posts.views import post_list, post_detail


urlpatterns = [

    path('', post_list),
    path('<int:pk>/', post_detail),

]


urlpatterns = format_suffix_patterns(urlpatterns)