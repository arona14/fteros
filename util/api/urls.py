from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls import url
from util.api.views import ConnectionSettingAPIView, ConnectionSettingRudView,FeedBackAPIView,FeedBackRudView

urlpatterns = [
    url( r'^connection/setting/$', ConnectionSettingAPIView.as_view(), name='connection-setting-create' ),
    url(r'^connection/setting/(?P<id>\d+)/$', ConnectionSettingRudView.as_view(), name='connection-setting-rud' ),
    url( r'^feedback/$', FeedBackAPIView.as_view(), name='create_feedback' ),
    url( r'^feedback/(?P<id>\d+)/$', FeedBackRudView.as_view(), name='FeedBack_rud')
    
]
