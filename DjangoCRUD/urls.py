from django.contrib import admin
from django.urls import path
from DjangoCRUD import views
urlpatterns = [
    path('add', views.add_person),
    path('', views.list_person),
    path('list', views.list_person),
    path('edit/<str:firstName>', views.edit_person),
    path('update/<str:firstName>', views.update_person),
    path('delete/<str:firstName>', views.delete_person),
]