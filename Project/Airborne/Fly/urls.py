from . import views
from django.urls import path
app_name = 'Fly'

urlpatterns = [
    path('', views.creation, name='creation'),
    path('Aircraft/<int:id>/', views.detail, name='detail'),
    path('add/', views.add_products, name='add'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete')
]