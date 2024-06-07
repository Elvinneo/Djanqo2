from django.urls import path
from users import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.profiles, name='users'),

]


