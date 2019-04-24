from django.urls import path

from . import views

urlpatterns = [
    path('login/display/', views.display, name='display'),
    path('login/display/insert.html', views.submit, name='submit'),
]
