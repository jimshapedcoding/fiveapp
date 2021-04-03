from django.urls import path
from codingsession import views

urlpatterns = [
    path('home/', views.codingsessionspage, name='codingsessionspage'),
]