from django.conf.urls import patterns, url

# This should contain urls related to CTiP ONLY
urlpatterns = patterns(
    # Forms Registry
    'cpovc_ctip.views',
    url(r'^$', 'ctip_home', name='ctip_home'),
    url(r'^case/(?P<case_id>[0-9A-Za-z_\-{32}\Z]+)/$',
        'view_ctip_case', name='view_ctip_case'),
    url(r'^form/(?P<form_id>[A-Z{1}\Z]+)/(?P<case_id>[0-9A-Za-z_\-{32}\Z]+)/(?P<id>\d+)/$',
        'ctip_forms', name='ctip_forms'),
    url(r'^form/(?P<form_id>[A-Z{1}\Z]+)/(?P<case_id>[0-9A-Za-z_\-{32}\Z]+)/$',
        'ctip_form', name='ctip_form'),
    url(r'^form/view/(?P<form_id>[A-Z{1}\Z]+)/(?P<case_id>[0-9A-Za-z_\-{32}\Z]+)/$',
        'view_ctip_form', name='view_ctip_form'),
    url(r'^new/(?P<case_id>[0-9A-Za-z_\-{32}\Z]+)/$',
        'new_ctip_case', name='new_ctip_case'),
    url(r'^edit/(?P<case_id>[0-9A-Za-z_\-{32}\Z]+)/$',
        'edit_ctip_case', name='edit_ctip_case'),

)
