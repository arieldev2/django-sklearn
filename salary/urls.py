from django.urls import path
from .views import SalarioListView, SalarioCreateView, SalarioDetailView, SalarioUpdateView, SalarioDeleteView

urlpatterns = [
	path('salario/', SalarioListView.as_view(), name='salario'),
	path('salario/create/', SalarioCreateView.as_view(), name='salario-create'),
	path('salario/detail/<int:pk>/', SalarioDetailView.as_view(), name='salario-detail'),
	path('salario/edit/<int:pk>/', SalarioUpdateView.as_view(), name='salario-edit'),
	path('salario/delete/<int:pk>/', SalarioDeleteView.as_view(), name='salario-delete'),
   
]