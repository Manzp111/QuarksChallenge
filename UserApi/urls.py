
from django.contrib import admin
from django.urls import path,include

from Users.views import users

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('Users.urls')),
]
