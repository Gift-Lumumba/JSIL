from django.conf.urls import url,include
from django.contrib import admin

app_name = "space"

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('space.urls'))
]