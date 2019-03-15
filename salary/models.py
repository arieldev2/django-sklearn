from django.db import models
from django.utils import timezone
from sklearn.externals import joblib
from django.urls import reverse
import numpy as np


class Salario(models.Model):
	experiencia = models.FloatField()
	salario_ex = models.FloatField()
	fecha = models.DateTimeField(default=timezone.now)

	def predict_salario(self):
		clf = joblib.load('salary/modelo.pkl')
		result = clf.predict([[self.experiencia]])
		return result


	def save(self, *args, **kwargs):
		self.salario_ex = self.predict_salario()
		super().save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('salario-detail', kwargs={'pk': self.pk})
