from django.urls import path
from . import views

urlpatterns = [
    path('', views.PageList, name='post_list'),
    path('offer/', views.PageDetailView, name="page")
]
