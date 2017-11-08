from django.conf.urls import url
from . import views
from tracking.views import InterviewerAutocomplete, InformationAutocomplete

app_name = 'tracking'
urlpatterns = [
    url(r'^f1/(?P<pid>[0-9]+)/$', views.form_1, name='form_1'),
    url(r'^f2/(?P<pid>[0-9]+)/$', views.form_2, name='form_2'),
    url(r'^f3/(?P<pid>[0-9]+)/$', views.form_3, name='form_3'),
    url(r'^information-autocomplete/$', InformationAutocomplete.as_view(), name='information-autocomplete', ),
    url(r'^interview-autocomplete/$', InterviewerAutocomplete.as_view(), name='interview-autocomplete', ),
    url(r'^input/$', views.input, name='input'),
]
