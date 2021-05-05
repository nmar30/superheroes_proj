from . import views
from django.urls import path

app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:superhero_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create'),
    path('delete=<int:superhero_id>/', views.delete, name='delete'),
    path('edit=<int:superhero_id>/', views.edit, name='edit'),
]
