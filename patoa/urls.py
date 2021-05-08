from django.urls import path
# from .views import scrape, dashboard
from .views import  dashboard, profile,patclaim, remov,clear
# from .views import  dashboard, profile,patclaim, clear
from  django.http import HttpResponse
from django.conf.urls import url

# def dashboard(request):
#     return HttpResponse('<h1> Dashboard <h1>')

app_name = 'patoa'

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    url(r'^user/(\w+)/$', profile, name='profile'),
    url(r'^patclaim/(\d+)/$', patclaim, name='patclaim'),
    url(r'^remov/(\d+)/$', remov, name='remov'),
    url(r'^clear/(\w+)/$', clear, name='clear'),

    # path('delete/',views.clear, name="clear")
 ]
