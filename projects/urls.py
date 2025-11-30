from django.urls import path
from .import views

urlpatterns  = [
    path('',views.home, name='home'),
    path('create/', views.project_create, name='project_create'),
    path('edit/<int:pk>/', views.project_edit, name='project_edit'),
    path('delete/<int:pk>/', views.project_delete, name='project_delete'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('download_cv/', views.download_cv, name='download_cv'),
     path('view_cv/', views.view_cv, name='view_cv'),
    
]