from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^login/$', login,{'template_name':'accounts/login.html'}),
    url(r'^cargo/', views.cargo_list, name = 'cargo'),
    url(r'^new/cargo$', views.new_cargo, name='new-cargo'),
    url(r'^update/cargo/(?P<pk>\d+)/$', views.update_cargo, name='update-cargo'),

]
