from django.conf.urls import patterns, include, url
from django.contrib import admin
from app.serializers import *
from app.views import DeviceRegisterView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/auth/$', EmailUserObtainAuthToken.as_view()),
    url(r'^api/messages/$', MessageList.as_view(), name='messages-list'),
    url(r'^api/messages/(?P<pk>[0-9]+)/$', MessageDetail.as_view(), name='messages-detail'),
    url(r'^api/chatters/$', ChatterList.as_view(), name='chatters-list'),
    url(r'^api/chatters/(?P<pk>[0-9]+)/$', ChatterDetail.as_view(), name='chatters-detail'),
    url(r'^api/register-push-token/$', DeviceRegisterView.as_view, name='device-token-register'),
)