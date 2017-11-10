from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from .views import input

urlpatterns = [
    # .com/        --> Index drop page
    url(r'^$', input, name='index'),
    # .com/home    --> home page
    url(r'^home/', include('home.urls')),
    # .com/admin   --> Admin Interface
    url(r'^admin/', admin.site.urls),

    # .com/results --> the results of the application
    url(r'^results/', TemplateView.as_view(template_name='results.html'), name='results'),
    url(r'^input/', input, name='input'),
]
