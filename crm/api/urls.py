from rest_framework_jwt.views import obtain_jwt_token
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from django.conf.urls import url
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from crm.api.views import *

urlpatterns = [
    url(r'^account/token/$', obtain_jwt_token),
    url(r'^account/token-verify/', verify_jwt_token),
    url(r'^account/token-refresh/', refresh_jwt_token),
    url(r'^account/user/create/$', UserCreateAPIView.as_view(), name='user-create' ),
    url(r'^account/users/$', UserListAPIView.as_view(), name='user-list' ),
    url(r'^account/users/(?P<id>\d+)/$', UserRudView.as_view(), name='user-rud' ),
    url(r'^account/resetpassword/(?P<id>\d+)/$', UserPasswordResetView.as_view(), name='user-reset-password' ),
    url(r'^account/updatepassword/$', UserUpdatePasswordView.as_view(), name='user-update-password' ),
    url(r'^affiliates/$', AffiliateAPIView.as_view(), name='affiliate-create' ),
    url(r'^affiliates/(?P<id>\d+)/$', AffiliateRudView.as_view(), name='affiliate-rud' ),
    url( r'^customers/$', CustomerAPIView.as_view(), name='customer-create' ),
    url( r'^customers/(?P<id>\d+)/$', CustomerRudView.as_view(), name='customer-rud' ),
    url(r'^airlines/$', AirlineAPIView.as_view(), name='airline-list' ),
    url( r'^airlinexceptions/$', ExceptionAirlineAPIView.as_view(), name='exception-create' ),
    url(r'^airlinexceptions/(?P<id>\d+)/$', ExceptionAirlineRudView.as_view(), name='airline-exeption-rud' ),
    url(r'^contracts/$', ContractAPIView.as_view(), name='contract-create' ),
    url(r'^contracts/(?P<id>\d+)/$', ContractRudView.as_view(), name='contract-rud' ),
    url(r'^markups/$', MarkupAPIView.as_view(), name='markup-list' ),
    url(r'^markups/(?P<id>\d+)/$', MarkupRudView.as_view(), name='markup-rud' ),
    url(r'^rewards/$', RewardAPIView.as_view(), name='reward-list' ),
    url(r'^rewards/(?P<id>\d+)/$', RewardRudView.as_view(), name='reward-rud' ),
    url(r'^customermarkups/$', CustomerMarkupAPIView.as_view(), name='customermarkup-list' ),
    url(r'^customermarkups/(?P<id>\d+)/$', CustomerMarkupRudView.as_view(), name='customermarkup-rud' ),
    url(r'^customerrewards/$', CustomerRewardAPIView.as_view(), name='customerreward-list' ),
    url(r'^customerrewards/(?P<id>\d+)/$', CustomerRewardRudView.as_view(), name='customerreward-rud' ),
    url(r'^dropnets/$', DropnetAPIView.as_view(), name='dropnet-list' ),
    url(r'^dropnets/(?P<id>\d+)/$', DropnetRudView.as_view(), name='dronet-rud' ),
    url(r'^communications/$', CommunicationAPIView.as_view(), name='communication-create' ),
    url(r'^communications/(?P<id>\d+)/$', CommunicationRudView.as_view(), name='traveler-rud' ),
    url(r'^signs/$', SignAPIView.as_view(), name='Sign-create' ),
    url(r'^signs/(?P<id>\d+)/$', SignRudView.as_view(), name='Sign-rud' ),
    url(r'^pcc/$', PccAPIView.as_view(), name='PCc-create' ),
    url(r'^pcc/(?P<id>\d+)/$', PCcRudView.as_view(), name='PCc-rud' ),
    url(r'^customerlist/$', UserCustomerListAPIView.as_view(), name='customerlist-create' ),
    url(r'^customerlist/(?P<id>\d+)/$', UserCustomerListRudView.as_view(), name='customerlist-rud' ),
    url(r'^customersaffiliated/$', CustomersAffiliateView.as_view(), name='Customers-Affiliate'),
    url(r'^userscustomersaffiliate/$', UsersCustomerAffiliateView.as_view(), name='Users-Customer-Affiliate'),
    url(r'^customersuser/$', IdUserCustomerView.as_view(), name='user-customers' ),
    url(r'^groups/$', GroupeAPIView.as_view(), name='group-create' ),
    url(r'^groups/(?P<id>\d+)/$', GroupeRudView.as_view(), name='group-rud' ),
    url(r'^customergroup/$', CustomerGroupAPIView.as_view(), name='customergroup-create' ),
    url(r'^customergroup/(?P<id>\d+)/$', CustomerGroupRudView.as_view(), name='customergroup-rud' ),
    
    
]


