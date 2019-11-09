from django.db import models

class patient(models.Model):
	pid = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=200,blank=True)
	email = models.EmailField(max_length=254,blank=True)
	age = models.IntegerField()
	acuity = models.IntegerField()  # visual acuity is used to mark vision for visually impaired people

class emergency(models.Model):
	eid=models.IntegerField(patient)
	state= models.IntegerField(default=0) # 0 or 1
	timestamp= models.DateTimeField()

class heartrate(models.Model):
	pid = models.IntegerField()
	ht = models.IntegerField()


	