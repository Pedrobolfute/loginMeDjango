from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('app_login.urls')),
    path('', lambda request: redirect('login/', permanent=True)),
    path('register/', include('app_create_account.urls')),
    path('change/', include('app_change_account.urls')), #Mudar para formulario
    path('welcome/', include('app_welcome.urls')),
    path('administrator/', include('app_admin.urls')),
]
