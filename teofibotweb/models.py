from __future__ import unicode_literals

from choices import *
from datetime import datetime

from django.db import models

class Tag(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(blank=True, null=True)
	def __str__(self):
		return self.name.encode('utf8')

class User(models.Model):
	full_name = models.CharField(max_length=200)
	tag = models.CharField(max_length=200, unique=True)
	def __str__(self):
		return self.full_name.encode('utf8')

class AutoResponse(models.Model):
	label = models.CharField(max_length=200)
	power = models.IntegerField(default=3, choices= POWER_CHOICES)
	message = models.TextField(blank=True, null=True)
	audio= models.CharField(blank=True, null=True, max_length=200)
	sticker= models.CharField(blank=True, null=True, max_length=200)

	def __str__(self):
		return self.label.encode('utf8')


class TextInputPattern(models.Model):
	label = models.CharField(max_length=200)
	regexp = models.TextField()
	type = models.IntegerField(default=2, choices= INPUT_TYPES)
	power = models.IntegerField(default=3, choices= POWER_CHOICES)

	response= models.ForeignKey(AutoResponse, blank=True, null=True)
	specialResponse= models.ForeignKey(AutoResponse, blank=True, null=True, related_name="specialResponse")
	senders= models.ManyToManyField(User, blank=True, null=True)

	def __str__(self):
		return self.label.encode('utf8')


class Sticker(models.Model):
	label = models.CharField(max_length=200, default="NOT LABELED")
	file_id = models.CharField(max_length=200, unique=True)
	file_path = models.CharField(max_length=200)
	is_cool= models.BooleanField(default=False)
	pub_date = models.DateTimeField('publication date', default=datetime.now)
	tags= models.ManyToManyField(Tag, blank=True, null=True)
	
	def image_tag(self):
	    return u'<img height="128px" width="128px" src="%s" />' % self.file_path

	image_tag.short_description = 'Image'
	image_tag.allow_tags = True

	def __str__(self):
		return self.label.encode('utf8')


class StickerResponse(models.Model):
	label = models.CharField(max_length=200, default="NOT LABELED")

	stickers= models.ManyToManyField(Sticker, blank=True, null=True, related_name="stickers")
	
	tags= models.ManyToManyField(Tag, blank=True, null=True)
	reply_tags= models.ManyToManyField(Tag, blank=True, null=True, related_name="replyTags")

	reply = models.TextField(blank=True, null=True)
	specialReply = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.label.encode('utf8')
