from django.conf.urls import include, url
from django.views.generic import TemplateView
from accounts.views import CustomRegistrationView
from . import views

urlpatterns = [
    url(r'^registration/register/$',
        CustomRegistrationView.as_view(),
        name='registration_register'
    ),
    url(r'^registration/', include('registration.backends.simple.urls')),
    url(r'^registration/', include('registration.auth_urls')),
    url(r'^teams/$', views.index, name='teams'),
    url(r'^team/$', views.team_detail, name='team'),
    url(r'^team/create/$', views.TeamCreateView.as_view(), name='team_create'),
    url(r'^team/(?P<pk>\w+)$', views.team_detail, name='team'),
    url(r'^user/$', views.user_detail, name='user'),
    url(r'^user/(?P<pk>\w+)$', views.user_detail, name='user'),

    #url(r'^user_test/$', views.user_detail_test, name='user'),
    #url(r'^user_test/(?P<pk>\w+)$', views.user_detail_test, name='user'),
    

    url(r'^no-team/$',
        TemplateView.as_view(template_name="accounts/no_team.html"),
        name='no_team'
    ),
    url(r'^no-profile/$',
        TemplateView.as_view(template_name="accounts/no_profile.html"),
        name='no_profile'
    ),
]
