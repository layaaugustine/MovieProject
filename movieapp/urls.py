from django.urls import path
from . import views

app_name = 'movieapp'
urlpatterns = [
    path('',views.Index.as_view(),name='index_page'),
    path('movie/<int:movie_id>/',views.Details.as_view(),name='detail_page'),
    path('add',views.addmovie,name='add_page'),
    path('update/<int:id>/',views.update,name='update_page'),
    path('delete/<int:id>/',views.delete,name='delete_page'),
]