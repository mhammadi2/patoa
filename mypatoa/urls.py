from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from patoa import views
from .views import  home_view, login_view, logout_view, register_view
from django.conf.urls import url

# def dashboard(request):
#     return HttpResponse('<h5> Dashboard <h5>')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('signin/', register_view, name='signin'),
    path('', include('patoa.urls', namespace='patoa')),
    # path('scrape/', views.scrape, name='scrape'),
    # path('delete/',views.clear, name="clear"),
    path('', views.dashboard, name="dashboard"),
    # path('dashboard/', dashboard, name="dashboard"),
    # url(r'^user/(\w+)/$', views.profile, name='profile'),
]
