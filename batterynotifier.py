# -*- coding: utf-8 -*-
"""
Created on Sun May 24 18:18:00 2020

@author: MeTaNa
"""

'''
this program is simple, notifys u if battery is fully charged,
'''

import psutil
from time import sleep
from win10toast import ToastNotifier
toaster = ToastNotifier()

while True:
	battery = psutil.sensors_battery()
	plugged = battery.power_plugged
	percent = str(battery.percent)
	if plugged==False: plugged="Not Plugged In"
	else: plugged="Plugged In"
	if (psutil.sensors_battery().power_plugged == True) and (battery.percent == 100):
		print(percent+'% | '+plugged)
		print('Unplug the Charger Please!')
		toaster.show_toast('Battery Statues','Battery Full.\nUnplug the Charger Please!')
		sleep(600)
	else:
		print(percent+'% | '+plugged)
		print('Thank Your.')
		toaster.show_toast('Battery Statues','Charger Not Plugged')
		sleep(3600)
