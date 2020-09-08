
from django.contrib import admin
from django.urls import path, include

from account.views import account_update_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('pages.urls')),
    path('account_modify/', account_update_view, name='modify_account'),
]
