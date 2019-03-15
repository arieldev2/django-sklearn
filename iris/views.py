from django.shortcuts import render, redirect
from .models import Medida
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
import csv
from django.urls import reverse
from os.path import join
from django.conf import settings
import codecs
import numpy as np




class IrisListView(ListView):
	model = Medida
	template_name = 'iris/list.html'
	context_object_name = 'items'
	ordering = ['-fecha']


class IrisCreateView(CreateView):
	model = Medida
	fields = ['largo_de_sepalo', 'ancho_de_sepalo', 'largo_de_petalo', 'ancho_de_petalo']


class IrisDetailView(DetailView):
	model = Medida


class IrisUpdateView(UpdateView):
	model = Medida
	fields = ['largo_de_sepalo', 'ancho_de_sepalo', 'largo_de_petalo', 'ancho_de_petalo']

class IrisDeleteView(DeleteView):
	model = Medida
	success_url = '/'
	



def add_csv(request):
	if request.method == 'POST':
		path = request.FILES['q']

		reader = csv.reader(codecs.iterdecode(path, 'utf-8'))
		for row in reader:
			_, created = Medida.objects.get_or_create(
				largo_de_sepalo=float(row[0]),
				ancho_de_sepalo=float(row[1]),
				largo_de_petalo=float(row[2]),
				ancho_de_petalo=float(row[3]),
	            )
			
		return redirect(reverse('list'))



