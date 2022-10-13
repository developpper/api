from django.urls import path
from . import views

from .views import sc


app_name = 'nss'

# api/v1/notes/
urlpatterns = [
    path('amazon-products/', views.amazon_products, name='amazon_products'),
    path('ap/', views.ap, name='ap'),
    # path('<int:pk>/', views.fs_detail, name='fs_detail'),
    path('amazon-product/<int:pk>/', views.showSingleAM, name='am_single'),
    path('item-remove/<str:id>/', views.notes_remove, name='notes_remove'),
    path('scrape/', views.scrape, name='scrape'),

    path('sc/', sc, name='sc'),

]