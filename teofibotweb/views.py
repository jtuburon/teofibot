from django.shortcuts import render
from django.http import HttpResponse
from subprocess import call

def send_once(device_id, message):
	call(['irsend', 'SEND_ONCE', device_id, message])

# Create your views here.
def control(request):
	command=request.GET.get('command', '')
	print command
	if command=="PWR_ON":
		print "PRENDERE TV"
		send_once("LG", "lg_power")
		print "PRENDI TV"
	return HttpResponse('OK')

