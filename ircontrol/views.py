from django.shortcuts import render

from django.shortcuts import render
from django.http import JsonResponse

from subprocess import call

from models import *

import re

def send_lirc_command(device_id, message):
	command =['irsend', 'SEND_ONCE', device_id] + re.split("\s+", message)
	print command
	call(command)

# Create your views here.

def index(request):
	devices= Device.objects.order_by('name')
	context ={"devices": devices}
	return render(request, 'ircontrol/index.html', context)


def control(request):
	device_name=request.GET.get('device', '')
	action_name=request.GET.get('action', '')

	if device_name!="":
		try:
			device= Device.objects.get(name=device_name)
			print device
			try:
				print action_name
				action= DeviceAction.objects.get(name= action_name, device=device)
				print action
				send_lirc_command(device.lirc_name, action.lirc_name)
				response = JsonResponse({'status': 'OK', 'status_msg': 'Command sent succesfully'})
			except DeviceAction.DoesNotExist:
				response = JsonResponse({'status': 'FAILED', 'status_msg': 'Action does not exist'})	
		except Device.DoesNotExist:
			response = JsonResponse({'status': 'FAILED', 'status_msg': 'Device does not exist'})	
	else:
		response = JsonResponse({'status': 'FAILED', 'status_msg': 'No device set'})
	
	return response

def render_device(request):
	device_name=request.GET.get('device', '')
	device= Device.objects.get(name=device_name)
	layout=[]
	actions= device.deviceaction_set.order_by('layout_row', 'layout_col')

	current_row_id=None
	current_row=None

	for a in actions:
		if a.layout_row!=current_row_id:
			current_row=[a]
			layout.append(current_row)
			current_row_id=a.layout_row
		else:
			current_row.append(a)
	context ={"device": device, "actions_layout": layout}
	return render(request, 'ircontrol/render_device.html', context)