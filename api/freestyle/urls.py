from django.urls import path
from . import views

app_name = 'freestyle'

# api/v1/notes/
urlpatterns = [
    # path('/', views.notes, name='notes'),
    # path('<int:pk>/', views.fs_detail, name='fs_detail'),
    path('<int:pk>/', views.showSingleFS, name='fs_detail'),
    path('<str:id>/', views.notes_remove, name='notes_remove'),
]