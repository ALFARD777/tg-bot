import os
import time
from tkinter import *
from datetime import datetime
from threading import Thread

root = Tk()
currentTime0 = datetime.now()
currentTime = currentTime0.strftime("%d/%m/%Y - %H:%M:%S")
root.title(f'Controller start time -> {currentTime}')

def startcommand(event):
	os.system('main.py')

def startbot(event):
	start.destroy()
	#th = Thread(target = startcommand, args = (event, ))
	#th.start()
	close.pack()

def closebot(event):
	print(f'[{currentTime}] Bot is closed!')
	root.destroy()

start = Button(root,text = 'Запуск бота',width = 100, height = 5,bg = 'white', fg= 'green')
start.bind('<Button-1>', startbot)
start.pack()

close = Button(root,text = 'Остановить бота',width = 100, height = 5,bg = 'white', fg = 'red')
close.bind('<Button-1>', closebot)

root.mainloop()