from django.urls import path
from .views import (
    all_utilisateurs_view,
    create_utilisateur_view,
    delete_utilisateur_view,
    update_utilisateur_view
)

urlpatterns = [
    path('list/', all_utilisateurs_view, name='list' ),
    path('create/', create_utilisateur_view, name='create'),
    path('delete/<int:id>', delete_utilisateur_view, name='delete'),
    path('update/<int:id>', update_utilisateur_view, name='update')
]