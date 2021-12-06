from django.db import models

class Student(models.Model):
	name = models.CharField(max_length = 200)
	roll = models.IntegerField()
	city = models.CharField(max_length = 100)

	def __str__(self):
		return self.name+' '+str(self.roll)


