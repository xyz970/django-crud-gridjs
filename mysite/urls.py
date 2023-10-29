"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path
from mysite.views import book
from mysite.views.api import fileHandling
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from mysite import settings

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', book.getBookData),
    path('book/detail/<str:slug>/', book.getBookDetail),
    path('book/insert/', book.insertPage,name="insertPage"),
    path('book/store', book.storeBookData, name="bookStore"),

    path('book/data/', book.getAllBook, name="getAllData"),
    path('book/search/<str:keyword>', book.filterBookData, name="searchData"),

    # handling form upload
    path('temp/store', fileHandling.uploadFile, name="tempUpload"),
    # re_path(r"^temp/revert/(?P<filename>[^/]+)/\\Z", fileHandling.revertFile, name="revertFile"),
    re_path(r"^temp/revert/(?P<filename>.*)", fileHandling.revertFile, name="revertFile"),
    path('temp/revert/', fileHandling.revertFile, name="revertFile"),
    # path('temp/revert/<filename>', fileHandling.revertFile, name="revertFile", kwargs={'filename': None})
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()


