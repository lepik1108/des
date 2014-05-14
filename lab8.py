from ball import *
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt
import time,math
	
class Engine:
	def __init__(self):
		plt.ion()
		plt.ylim((-100,100))
		plt.xlim((-1,1))
		self.graphic, = plt.plot([], [], 'ro')
		self.is_stoped = False
		
	def start(self, obj):
		while(False == self.is_stoped):
			obj.recalc()
			X,Y = obj.array()
			time.sleep(0.01)
			self.graphic.set_xdata(X)
			self.graphic.set_ydata(Y)
			plt.draw()
			
	def stop():
		self.is_stoped = True

e = Engine()
obj = Bal(0,10)
obj.setEngine(e)
e.start(obj)
