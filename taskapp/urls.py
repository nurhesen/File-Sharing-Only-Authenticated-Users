from django.urls import path
from .views import *

app_name='taskapp'

urlpatterns = [
    path('', Home,name='home'),
    path('detail/<int:pk>/', FaylDetail.as_view(),name='detail'),
    path('create', FaylCreateView.as_view(),name='create'),
    path('paylas', PaylasView.as_view(),name='paylas'),
    path('register', RegisterView,name='register'),
    path('login', LoginView.as_view(),name='login'),

    
]
