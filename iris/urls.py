from django.urls import path
from .views import IrisCreateView, IrisListView, add_csv, IrisDetailView, IrisUpdateView, IrisDeleteView

urlpatterns = [
  path('', IrisListView.as_view(), name='list'),
  path('create/', IrisCreateView.as_view(), name='create'),
  path('detail/<int:pk>/', IrisDetailView.as_view(), name='detail'),
  path('edit/<int:pk>/', IrisUpdateView.as_view(), name='edit'),
  path('delete/<int:pk>/', IrisDeleteView.as_view(), name='delete'),
  path('add/', add_csv, name='add'),


]
