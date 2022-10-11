from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add_image', views.ImageView.as_view(), name='add_image')
]