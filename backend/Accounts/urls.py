from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from Accounts.views import account_list, account_login


urlpatterns = [

    path('', account_list),    
    path('login/',account_login),

]


urlpatterns = format_suffix_patterns(urlpatterns)