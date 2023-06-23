from django.urls import path
from searchapp import views

urlpatterns = [
    path('', views.search, name='search'),
]
