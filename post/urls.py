from django.urls import path
from . import views

urlpatterns = [
  path('add-post/', views.add_post, name='add-post') ,
  path('edit-post/<int:id>/', views.edit_post, name="edit-post"), 
  path('delete-post/<int:id>/', views.delete_post, name="delete-post") 
]
