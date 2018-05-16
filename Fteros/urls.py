"""
Definition of urls for Fteros.
"""

from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf import settings
from django.urls import reverse_lazy
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', Fteros.views.home, name='home'),
    # url(r'^Fteros/', include('Fteros.Fteros.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^password_reset/$', PasswordResetView.as_view(), name='password_reset'),
    url(r'^password_reset/done/$', PasswordResetDoneView.as_view(), name= 'password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset/done/$', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    url(r'^api/crm/', include('crm.api.urls', namespace='api-crm')),
    url(r'^api/gds/', include('gds.api.urls', namespace='api-gds')),
    url(r'^api/util/', include('util.api.urls', namespace='api-util')),
    url(r'^auth/', include('rest_auth.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
