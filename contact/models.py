from django.db import models
from django.utils.timezone import now

class Contact(models.Model):
	name = models.CharField(max_length = 200)
	email = models.EmailField(max_length=254)
	message = models.TextField()
	created_at = models.DateTimeField(default = now)

	def __str__(self):
		return self.name

	def msg(self):
		return self.message[:35]+'...'
