from django.shortcuts import render
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from .models import Salario


class SalarioListView(ListView):
	model = Salario
	template_name = 'salary/salary_list.html'
	context_object_name = 'items'
	ordering = ['-fecha']

class SalarioCreateView(CreateView):
	model = Salario
	fields = ['experiencia']
	

class SalarioDetailView(DetailView):
	model = Salario

class SalarioUpdateView(UpdateView):
	model = Salario
	fields = ['experiencia']

class SalarioDeleteView(DeleteView):
	model = Salario
	success_url = '/salario'
