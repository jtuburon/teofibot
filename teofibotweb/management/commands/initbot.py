# coding=utf-8

from django.core.management.base import BaseCommand, CommandError

from core.teofibot import TeofiBot

class Command(BaseCommand):
	help = 'Initialize TeofiBot'

	def handle(self, *args, **options):
		TeofiBot()