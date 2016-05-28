from django.conf.urls import patterns, url, include

urlpatterns = patterns(
    'api.views',

    url(r'^users/$',
        'register_user',
        name='register_user'),

    url(r'^login/$',
        'user_login',
        name='user_login'),
)

#TODO: Purpose of this Line
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
