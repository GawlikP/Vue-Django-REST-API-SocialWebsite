from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from comments.views import comments_list, comments_detail

urlpatterns = [

    path('', comments_list),
    path('<int:pk>/', comments_detail),

]

urlpatterns = format_suffix_patterns(urlpatterns)