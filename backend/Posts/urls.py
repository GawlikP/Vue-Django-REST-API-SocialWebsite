from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Posts.views import post_list


urlpatterns = [

    path('', post_list),

]


urlpatterns = format_suffix_patterns(urlpatterns)