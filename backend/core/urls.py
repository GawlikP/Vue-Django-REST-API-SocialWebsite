from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import accounts_list, auth_test_view, accounts_login, check_token, account_defails
from .views import account_hearts, account_profile
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', accounts_list, name='account basic jobs'),
    path('im_auth/', auth_test_view, name='testing auth url'),
    path('login/', accounts_login, name='accont login job'),
    path('tokencheck/', check_token, name='checking if token exist'),
    path('<int:pk>/', account_defails, name='operations on instance of user'),
    path('hearts/', account_hearts, name='geting hearts belonging to account'),
    path('profile/', account_profile, name='geting account profile'),
    path('commentslikes/', account_commentslikes, name='geting likes that belongs to acount')
]

urlpatterns = format_suffix_patterns(urlpatterns)