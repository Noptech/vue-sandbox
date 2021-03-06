from django.conf.urls import include, url

from . import views
from rest_framework.authtoken import views as drf_views
from rest_framework.authtoken.views import obtain_auth_token


app_name = 'vcta_service_rest'
urlpatterns = [
    url(r'^hero/$', views.HeroList.as_view(), name='hero_list'),
    url(r'^hero/(?P<pk>\d+)$', views.HeroDetail.as_view(), name='hero_detail'),
    url(r'^trip/$', views.TripList.as_view(), name='trip_list'),
    url(r'^trip/(?P<pk>\d+)$', views.TripDetail.as_view(), name='trip_detail'),
    url(r'^team/$', views.TeamList.as_view(), name='team_list'),
    url(r'^team/(?P<pk>\d+)$', views.TeamDetail.as_view(), name='team_detail'),
    url(r'^user/$', views.UserList.as_view(), name='user_list'),
    url(r'^user/(?P<pk>\d+)$', views.UserDetail.as_view(), name='user_detail'),
    url(r'^config/$', views.ConfigList.as_view(), name='config_list'),
    url(r'^config/(?P<pk>\d+)$', views.ConfigDetail.as_view(), name='config_detail'),

    url(r'^custom/', include('vcta_service.custom_urls')),

    url(r'^auth$', drf_views.obtain_auth_token, name='auth'),
    url(r'^obtain-auth-token/$', obtain_auth_token)
]
