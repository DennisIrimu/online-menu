from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.food_list, name='food_list'),
    url(r'^(?P<category_slug>[-\w]+)/$',views.food_list, name='food_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$',views.food_detail,name='food_detail'),
]
