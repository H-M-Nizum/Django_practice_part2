from django.urls import path
from . import views

urlpatterns = [
    # path('', views.add_post, name='add_post'),
    # class base view
    path('', views.Addpostcreateview.as_view(), name='add_post'),
    # path('edit/<int:id>', views.edit_post, name='edit_post'),
    # class base view
    path('edit/<int:id>/', views.edit_post_view.as_view(), name='edit_post'),
    # path('delete/<int:id>', views.delete_post, name='delete_post'),
    # class base view
    path('delete/<int:id>/', views.delete_post_view.as_view(), name='delete_post'),
    path('details/<int:pk>/', views.post_details_view.as_view(), name='details_post'),
]