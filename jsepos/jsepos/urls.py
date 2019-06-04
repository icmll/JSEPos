"""JSEPos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from sale.views import TestView
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('JSEPos/admin/', admin.site.urls),
    path('JSEPos/api-auth/', include('rest_framework.urls')),

    path(r'JSEPos/sale/', include('sale.urls')),
    path(r'JSEPos/goods/', include('goods.urls')),

    path(r'JSEPos/docs', include_docs_urls(title=u'接口文档')),
    path(r'JSEPos/swg-docs', schema_view),

    re_path('JSEPos/test/', TestView.as_view()),
]
