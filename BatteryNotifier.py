# -*- coding: utf-8 -*-
"""
Created on Sun May 24 18:18:00 2020

@author: MeTaNa
"""

'''
this program is simple, notifys u if battery is fully charged,
'''

from tkinter import *
import os
import psutil
import win10toast

full_timer = 600000
chrg_timer = 3600000
nchrg_timer = 3600000

global battery
global plugged
global percent
battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = str(battery.percent)

if plugged == False:
	chrgr = "Not Plugged In"
else:
	chrgr = "Plugged In"

# baraye in k barname hamun aval hichkari nakne, faqat gui baz bshe.
def preload():
	pass

#vaziate batrio chk mikne:
def start():
	battery = psutil.sensors_battery()
	plugged = battery.power_plugged
	percent = str(battery.percent)
	if plugged == False:
		plugged = "Not Plugged In"
	else:
		plugged = "Plugged In"
	if (psutil.sensors_battery().power_plugged == True) and (battery.percent == 100):
		print(percent + '% | ' + plugged)
		print('Unplug the Charger Please!')
		win10toast.ToastNotifier().show_toast('Battery Statues', 'Battery Full.\nUnplug the Charger Please!', icon_path='bat.ico', duration=10, threaded=True)
		gui.after(full_timer, start)
	elif (psutil.sensors_battery().power_plugged == False) and (battery.percent != 100):
		print(percent + '% | ' + plugged)
		print('Not Charging...')
		win10toast.ToastNotifier().show_toast('Battery Statues', 'Charger Not Plugged', icon_path='bat.ico', duration=10, threaded=True)
		gui.after(chrg_timer, start)
	else:
		print(percent + '% | ' + plugged)
		print('Charging...')
		win10toast.ToastNotifier().show_toast('Battery Statues', 'Charging...', icon_path='bat.ico', duration=10, threaded=True)
		gui.after(nchrg_timer, start)

#m3 qabli, ama barname maxfiam mishe.
def start_tray():
	start()
	gui.withdraw()


#barname va script ro stop mikne o mibande kolan
def closer():
	try:
		os.system('TASKKILL /F /IM Bat2.exe')
		os.system('TASKKILL /F /IM BatteryNotifier.exe')
	except Exception:
		print('already closed!')
	gui.destroy()

#barname ro maxfi mishe.
def tray():
	gui.withdraw()

#menu about
def about():
	messagebox.showinfo('About', 'Written by MeTaNa!\nThis program notifies you\nwhen battery is ')

# create a GUI window
gui = Tk()
gui.resizable(False, False)
gui.geometry("530x80")
gui.configure(background="#f3f3f3")
gui.title("Battery Notifier")
gui.iconbitmap('bat.ico')


#dokme ha va labelL
label1 = Label(gui,text = 'Battery Notifier: ', font='mitrea')
label1.grid(row=0, column=0)
label2 = Label(gui,text = 'Battery Level is: ', font='mitrea')
label2.grid(row=1, column=0)
label3 = Label(gui,text = percent+' % and', font='mitrea')
label3.grid(row=1, column=1)
label4 = Label(gui,text = 'Charger is ', font='mitrea')
label4.grid(row=1, column=2)
label5 = Label(gui,text = chrgr, font='mitrea')
label5.grid(row=1, column=3)

button1 = Button(gui, text=' Start Script ', fg='white', bg='gray', command=start, height=2, width=9)
button1.grid(row=0, column=1)
button2 = Button(gui, text=' Start + Tray ', fg='white', bg='gray', command=start_tray, height=2, width=9)
button2.grid(row=0, column=2)
button3 = Button(gui, text=' Stop Script ', fg='white', bg='gray', command=closer, height=2, width=9)
button3.grid(row=0, column=3)
button4 = Button(gui, text=' About ', fg='white', bg='gray', command=about, height=2, width=9)
button4.grid(row=0, column=4)
button5 = Button(gui, text=' Tray ', fg='white', bg='gray', command=tray, height=2, width=9)
button5.grid(row=0, column=5)


# start the GUI
gui.after(100, preload)
gui.mainloop()
gui.update_idletasks()
