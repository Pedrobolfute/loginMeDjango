from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('app_login.urls')),
    path('register/', include('app_create_account.urls'))
]
