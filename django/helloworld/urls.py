"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""三种写法：
   1.path只能绝对匹配路径地址，不支持正则匹配。匹配规则是RoutePattern
   2.re_path支持正则匹配，django 1.x版本常用。匹配规则是RegexPattern
   3.url支持正则匹配，实际上就是return re_path, django2.x版本推荐
   url是部分动态
   页面有分页情况时，不能写死。可通过正则\d+ 匹配
   例：url('^demo/page=\d+$', views.demo)
"""
# # 默认demo
# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import re_path, path
from . import view
from hello import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'cards', views.CardViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^accounts/login/', views.login),
    url(r'^admin/', admin.site.urls),
    url(r'^$', view.index),
    url(r'^test$', view.test),
    url(r'^$', views.index),
    url(r'^demo', views.demo, name="demo_page"),
    url(r'^home$', views.home, name="home_page"),
    url('^demo/page=(\d+)$', views.page),
    path("archive/<year>/<month>.html", views.home1),   # 获取url参数，匹配 archive/2018/10.html
    url(r'^archive1/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2}).html$', views.home2),  # 通过正则匹配url, archive1/2018/10.html
    path("yoyo/", views.yoyo),
    path("page1/", views.page1),
    path("sonpage/", views.sonpage),
    path("get_demo/", views.get_demo),
    url(r'^qq/', views.test_qq),
    url(r'^result/', views.result_qq),
    url(r'^user/', views.user),
    url(r'^register/', views.register),  # 新增用户
    url(r'^reset/', views.reset_psw),
]