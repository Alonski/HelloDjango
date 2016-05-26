"""hellodjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse, JsonResponse


def home_page(request):
    # assert False, request.META['HTTP_USER_AGENT']
    # return HttpResponse("Hello <b>World!</b>", content_type="text/plain")
    return HttpResponse("Hello <b>World!</b>")
    # return JsonResponse({
    #     'a':'b',
    #     'c':'d',
    # })

def age(request, name, value):  # view function
    return HttpResponse("{}, you are {} years old".format(name.title(), value))


def mult(request, first, second):
    return HttpResponse("{} X {} = {}".format(first, second, (int(first) * int(second))))


def throw_404(request):
    return HttpResponse("404 Error", status=404)


# def go(request):
#     assert False, request.GET


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^age/(?P<name>\w+)/(?P<value>\d+)/$', age),
    url(r'^mult/(?P<first>\d+)/(?P<second>\d+)/$', mult),
    url(r'^$', home_page),
    url(r'$', throw_404),
    # url(r'age/(\w+)/$', age),
]
