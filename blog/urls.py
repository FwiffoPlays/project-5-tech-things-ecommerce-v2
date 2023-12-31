from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('update/<int:blog_id>/', views.update, name='update'),
    path('delete/<int:blog_id>/', views.delete, name='delete'),
]
