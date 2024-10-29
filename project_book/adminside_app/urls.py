from django.urls import path
from . import views
urlpatterns = [
    path('admin_dashboard/',views.admin_dashboard, name='admin_dashboard'),
    path('admin_users/',views.admin_users,name='admin_users'), 
    path('add_users/',views.add_users, name='add_users'),
    path('view_users/',views.view_users, name='view_users'),
    path('admin_category/',views.admin_category, name='admin_category'),
    path('add_category/',views.add_category, name='add_category'),
    path('edit_category/',views.edit_category, name='edit_category'),
    path('delete_category/',views.delete_category, name='delete_category'),
    path('admin_products/',views.admin_products, name='admin_products'),
    path('add_products/',views.add_products, name='add_products'),
]