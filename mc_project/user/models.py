from django.db import models
from moniter.models import patient

class emergency(models.Model):
	pid = models.ForeignKey(patient, on_delete=models.CASCADE)
	state= models.IntegerField(default=0) # 0 or 1
	timestamp= models.DateTimeField()


	