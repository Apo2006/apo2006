from django.urls import path
from .views import register_view, login_view, logout_view

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
from django.urls import path
from .views import (
    register_view, login_view, logout_view,
    profile_view, address_add, address_edit, address_delete
)

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('profile/', profile_view, name='profile'),
    path('address/add/', address_add, name='address_add'),
    path('address/<int:pk>/edit/', address_edit, name='address_edit'),
    path('address/<int:pk>/delete/', address_delete, name='address_delete'),
]
