from django.urls import path
from .views import create_user, get_user

urlpatterns = [
    path('', create_user),          # POST
    path('api/users/<int:id>/', get_user_detail),   # GET by ID
]
