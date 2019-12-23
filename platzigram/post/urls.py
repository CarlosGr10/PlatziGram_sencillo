#Django
from django.urls import path

#Views
from post import views

urlpatterns = [

    path(
        route='',
        view=views.lista_post,
        name='feed'
    ),

    path(
        route='posts/new/',
        view=views.create_post,
        name='create_post'
    ),
]