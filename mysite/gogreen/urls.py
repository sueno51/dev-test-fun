from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /gogreen/
    url(r'^$',views.index,name='index'),
    # ex: /gogreen/5/
    url(r'^(?P<question_id>[0-9]+)/$',views.locationdetail,name='locationdetail'),
    # ex: /gogreen/5/locationinfo/
    url(r'^(?P<question_id>[0-9]+)/locationinfo/$',views.locationinfo,name='locationinfo'),
    # ex: /gogreen/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote')
]
