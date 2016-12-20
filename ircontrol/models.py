from __future__ import unicode_literals
from choices import *

from django.db import models


# Create your models here.

class Device(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(blank=True, null=True)
	type = models.IntegerField(default=1, choices= DEVICE_TYPES)
	location = models.IntegerField(default=1, choices= DEVICE_LOCATIONS)
	lirc_name = models.CharField(max_length=200)

	def __str__(self):
		return self.name.encode('utf8')

class DeviceAction(models.Model):
	name = models.CharField(max_length=200)
	rc_button_name = models.CharField(max_length=200, blank=True, null=True)
	lirc_name = models.CharField(max_length=400)
	device = models.ForeignKey(Device)

	def __str__(self):
		return self.name.encode('utf8')
