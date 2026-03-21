from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('membros/novo/', views.member_create, name='member_create'),
    path('membros/<int:id>/editar/', views.member_edit, name='member_edit'),
    path('membros/<int:id>/deletar/', views.member_delete, name='member_delete'),
    path('membros/<int:member_id>/ativo/novo/', views.asset_create, name='asset_create'),
    path('ativos/<int:id>/editar/', views.asset_edit, name='asset_edit'),
    path('ativos/<int:id>/deletar/', views.asset_delete, name='asset_delete'),
]