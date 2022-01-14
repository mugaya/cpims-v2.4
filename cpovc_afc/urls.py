from django.conf.urls import patterns, url

# This should contain urls related to Care reforms ONLY
urlpatterns = patterns(
    # Alternative Care
    'cpovc_afc.views',
    url(r'^$', 'alt_care_home', name='alternative_care'),
    url(r'^new/(?P<case_id>[0-9A-Za-z_\-{32}\Z]+)/$',
        'new_alternative_care', name='new_alt_care'),
    url(r'^view/(?P<case_id>[0-9A-Za-z_\-{32}\Z]+)/$',
        'view_alternative_care', name='view_alt_care'),
    url(r'^edit/(?P<case_id>[0-9A-Za-z_\-{32}\Z]+)/$',
        'edit_alternative_care', name='edit_alt_care'),
    url(r'^(?P<cid>[A-Z{2}\Z]+)/(?P<form_id>\d+[A-Z_\-{1}\Z]+)/(?P<case_id>[0-9A-Za-z_\-{32}\Z]+)/$',
        'alt_care_form', name='alt_care_form'),
)
