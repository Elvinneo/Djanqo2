from django.urls import path
from users import views
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('users/', views.profiles, name='users'),
    path('detail/<int:id>', views.detail, name='detail'),

]


