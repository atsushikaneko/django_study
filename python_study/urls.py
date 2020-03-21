from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    # http://127.0.0.1:8000/の直下のhelloworldに接続するとhelloworldアプリのurls.pyを呼び出す。
    url(r'^helloworld/', include('helloworld.urls')),
]