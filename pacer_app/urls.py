from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('score/<int:user_id>', views.get_score, name='score'),
]