# coding=utf-8

from telegram.ext import Updater
from telegram.ext import MessageHandler, Filters

import codecs

import os
import re
import logging
import urllib
from pydub import AudioSegment

from core.photo_ops import *
from teofibotweb.models import *

import random

class TeofiBot():	
	spammer=False
	ME= "TeoGol29"
	store_user=True
	store_sticker=True

	def __init__(self):
		self.start_bot()

	def get_resource_path(self, type,  audio_filename):
		return "resources/"+ type+ "/" + audio_filename

	def validate_user(self, senders, username):
		users=[s.tag for s in senders]
		
		valid=False

		if len(users)==1:
			if users[0]=="@ALL":
				valid= True
			if users[0]=="@NOT_ME" and username!= self.ME:
				valid= True
		if valid==False:
			valid =username in users
		specialResponse= username==self.ME
		return (valid, specialResponse)

	def get_random_reply_sticker(self, sticker_id, sticker_response):
		sticker= Sticker.objects.get(file_id=sticker_id)
		print sticker
		tags=sticker_response.reply_tags.all()
		stickers= Sticker.objects.filter(tags__in= tags).exclude(file_id=sticker_id)
		s = random.choice(stickers)
		return s

	def responseToAStickerCachonism(self, bot, update):
		message= update["message"]
		sticker= message["sticker"]

		user= message.from_user["username"]
		if user=="":
			user= message.from_user["first_name"]
		
		try:
			sticker_response = StickerResponse.objects.get(stickers__file_id=sticker.file_id)		
			reply_sticker= self.get_random_reply_sticker(sticker.file_id, sticker_response)
		except:
			sticker_response=None

		if sticker_response!=None:			
			if user not in [self.ME]:
				responseText= sticker_response.reply % user
			else:
				responseText= sticker_response.specialReply % user
			bot.sendMessage(chat_id=update.message.chat_id, text=responseText)
			bot.sendSticker(chat_id=update.message.chat_id, sticker=reply_sticker.file_id)
		else:
			sticker= bot.getFile(sticker.file_id)
			self.save_sticker(sticker);


	def save_user(self, username, full_name):
		u =User(tag=username, full_name=full_name)
		try:
			u.save()
		except:
			pass

	def save_sticker(self, sticker):
		s =Sticker(file_id= sticker.file_id, file_path=sticker.file_path)
		try:
			s.save()
		except:
			pass


	def responseToATextCachonism(self, bot, update):
		message= update["message"]
		
		full_name=message.from_user["first_name"] + " "+ message.from_user["last_name"] 
		user= message.from_user["username"]
		
		if user=="":
			user= full_name

		if self.store_user:
			self.save_user(user, full_name);
		
		patterns= TextInputPattern.objects.all()
		for p in patterns:
			if re.search(p.regexp, message.text, re.IGNORECASE) !=None:
		
				senders= p.senders.all()

				valid_user, specialResponse=self.validate_user(senders, user)
				
				if valid_user:
					if specialResponse==False:
						if p.response!=None:					
							r= p.response
					else:
						if p.specialResponse!=None:					
							r= p.specialResponse

					if r!=None:
						if r.message!=None and r.message!="":
							responseText= r.message % user
							bot.sendMessage(chat_id=update.message.chat_id, text=responseText)
						
						if r.audio!=None and r.audio!="":			
							audio_path= self.get_resource_path("sounds", r.audio)
							audio=open(audio_path.encode('utf-8'), 'rb')
							bot.sendAudio(chat_id=update.message.chat_id, audio=audio , caption='TeofiBot saboteandote con sabor')

						if r.photo!=None and r.photo!="":
							photo_path=self.get_resource_path("pics", r.photo)
							photo=open(photo_path.encode('utf-8'), 'rb')
							print photo
							bot.sendPhoto(chat_id=update.message.chat_id, photo=photo)
							print "mande"

						if r.document!=None and r.document!="":
							document_path=self.get_resource_path("documents", r.document)
							document=open(document_path.encode('utf-8'), 'rb')
							print document
							bot.sendDocument(chat_id=update.message.chat_id, document=document)
							print "mande"

						if r.sticker!=None and r.sticker!="":
							sticker_id=r.sticker
							bot.sendSticker(chat_id=update.message.chat_id, sticker=sticker_id)


				

	def responseToAPhotoCachonism(self, bot, update):
		message= update["message"]
		user= message.from_user["username"]
		if user=="":
			user= message.from_user["first_name"]
		responseText= "Hey %s. Soy TeofiBot, No mas stickers tontrones. Manda algo de sabor como esto..." % user
		downPhoto= bot.getFile(message.photo[-1].file_id)
		urllib.urlretrieve (downPhoto.file_path, downPhoto.file_id)
		status = addSmiles(downPhoto.file_id)
		if status[0]:
			bot.sendPhoto(chat_id=update.message.chat_id, photo=open(status[1], 'rb'), caption='TeofiBot con sabor')
			os.remove(status[1])
		os.remove(downPhoto.file_id)

	def responseToAnAudioCachonism(self, bot, update):
		message= update["message"]
		user= message.from_user["username"]
		if user=="":
			user= message.from_user["first_name"]

		responseText= "Hey %s. Soy TeofiBot. Mira lo que hago con tu nota de voz..." % user
		
		if user not in ["TeoGol29"]:		
			downAudio= bot.getFile(message.voice.file_id)
			urllib.urlretrieve (downAudio.file_path, downAudio.file_id)
			
			sound1 = AudioSegment.from_file(downAudio.file_id)
			source_path= self.get_resource_path("sounds", "mi_creador.mp3")
			sound2 = AudioSegment.from_file(source_path)

			sound1 = sound1 + 1
			sound2 = sound2 - 8
			combined = sound1.overlay(sound2)
			audio_mix_filename="mix_"+downAudio.file_id
			combined.export(audio_mix_filename , format='mp3')
			bot.sendMessage(chat_id=update.message.chat_id, text=responseText)
			bot.sendAudio(chat_id=update.message.chat_id, audio=open(audio_mix_filename, 'rb'), caption='TeofiBot saboteandote con sabor')
			os.remove(downAudio.file_id)
			os.remove(audio_mix_filename)
		
	def start_bot(self):
		logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

		updater = Updater(token='230721037:AAFoiOPvOkvOHdVfF5Bi0veAS7qtaueIX0M')
		dispatcher = updater.dispatcher

		sticker_handler = MessageHandler([Filters.sticker], self.responseToAStickerCachonism)
		dispatcher.add_handler(sticker_handler)

		pic_handler = MessageHandler([Filters.photo], self.responseToAPhotoCachonism)
		dispatcher.add_handler(pic_handler)

		text_handler = MessageHandler([Filters.text], self.responseToATextCachonism)
		dispatcher.add_handler(text_handler)

		audio_handler = MessageHandler([Filters.voice], self.responseToAnAudioCachonism)
		dispatcher.add_handler(audio_handler)

		updater.start_polling(clean=True)

		if self.spammer==True:
			from telegram.ext import Job
			j = updater.job_queue

			def grillos_test_job(bot, job):
				bot.sendMessage(chat_id=-158464518, text=u'Virgilio con los ahorros de Adrian  compró, por cuotas, al Clara Stereo y le pagó al Pambe de la siguiente manera: la primera semana abonó 3/8 de su chonchito, la segunda semana 1/6 y canceló en la tercera semana 2.200 pesos. ¿Por cuántos pesos que se sopló el lelo, Regina lo quiere disfrazar de puerco?')

			job_minute = Job(grillos_test_job, 300.0)
			j.put(job_minute, next_t=0.0)