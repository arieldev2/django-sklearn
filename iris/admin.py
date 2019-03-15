from django.contrib import admin
from .models import Medida


class AdminView(admin.ModelAdmin):
	list_display = ('id', 'largo_de_sepalo', 'ancho_de_sepalo', 'largo_de_petalo', 'ancho_de_petalo', 'prediccion')
	search_fields = ('id', 'prediccion',)
	




admin.site.register(Medida, AdminView)
