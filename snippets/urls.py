from django.conf.urls import url
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<id>[0-9]+)/$', views.SnippetList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
