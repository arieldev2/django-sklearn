from django.db import models
from django.utils import timezone
from sklearn.externals import joblib
from django.urls import reverse
import numpy as np





class Medida(models.Model):
	largo_de_sepalo = models.FloatField()
	ancho_de_sepalo = models.FloatField()
	largo_de_petalo = models.FloatField()
	ancho_de_petalo = models.FloatField()
	prediccion = models.IntegerField()
	fecha = models.DateTimeField(default=timezone.now)


	
	def predict_iris(self):
		clf = joblib.load('iris/modelo_entrenado.pkl')
		result = clf.predict([[self.largo_de_sepalo, self.ancho_de_sepalo, self.largo_de_petalo, self.ancho_de_petalo]])
		return result


	def save(self, *args, **kwargs):
		self.prediccion = self.predict_iris()
		super().save(*args, **kwargs)


	def get_absolute_url(self):
		return reverse('detail', kwargs={'pk': self.pk})



