from django.urls import path
from . import views
from .views import account

urlpatterns = [
    path('account/', account, name='account'),
    path('account/create/', views.create_profile_view, name='account_create'),
]
