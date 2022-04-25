from django.urls import path
from . import views
app_name='movieapp'
urlpatterns = [
    path('', views.index,name='index'),
    path('movie/<int:id>', views.details,name='detail'),
    path('add', views.add,name='add'),
    path('update/<int:id>', views.update,name='update'),
    path('delete/<int:id>', views.delete,name='delete'),
]