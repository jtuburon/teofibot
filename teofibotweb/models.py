from __future__ import unicode_literals

from choices import *

from django.db import models

class User(models.Model):
	full_name = models.CharField(max_length=200)
	tag = models.CharField(max_length=200, unique=True)
	def __str__(self):
		return self.full_name

class AutoResponse(models.Model):
	label = models.CharField(max_length=200)
	power = models.IntegerField(default=3, choices= POWER_CHOICES)
	message = models.TextField(blank=True, null=True)
	audio= models.CharField(blank=True, null=True, max_length=200)
	sticker= models.CharField(blank=True, null=True, max_length=200)

	def __str__(self):
		return self.label


class TextInputPattern(models.Model):
	label = models.CharField(max_length=200)
	regexp = models.TextField()
	type = models.IntegerField(default=2, choices= INPUT_TYPES)
	power = models.IntegerField(default=3, choices= POWER_CHOICES)

	response= models.ForeignKey(AutoResponse, blank=True, null=True)
	specialResponse= models.ForeignKey(AutoResponse, blank=True, null=True, related_name="specialResponse")
	senders= models.ManyToManyField(User, blank=True, null=True)

	def __str__(self):
		return self.label

