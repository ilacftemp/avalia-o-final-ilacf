from django.urls import path

from . import views

urlpatterns = [
    path('api/filmes/<str:titulo>/', views.api_filme),
    path('api/filmes/<str:titulo>/<str:palavra>/', views.delete_word),
    path('api/funfacts', views.facts),
    path('api/funfacts/<int:id>', views.deletefact),
    path('api/anuncios', views.anuncios),
    path('api/anuncios/<int:id>', views.update_anuncio),
]