import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import time,math

class Point:
	def __init__(self, x, y):
		self.x_ = x
		self.y_ = y
	def x(self):
		return self.x_
	
	def y(self):
		return self.y_

	def distance(self, point):
		return math.sqrt((self.x() - point.x())**2 + (self.y() - point.y())**2)
		
class Cloud():
	def __init__(self, points = None):
		if(points == None):
			self.points_ = []
		else:
			self.points_ = points
		self.c = None
	
	def addPoint(self, point):
		self.points_.append(point)
		self.c = None
	
	def center(self):
		if (self.c != None):
			return self.c
		sx = 0
		sy = 0
		length = len(self.points_)
		for point in self.points_:
			sx += point.x()
			sy += point.y()
		self.c = Point(sx/length, sy/length )
		return self.c
		
	def Points(self):
		if (len(self.points_) > 0):
			return map (lambda point: (point.x(),point.y()), self.points_)
		return []
	def Xs(self):
		if (len(self.points_) > 0):
			return map (lambda point: point.x(), self.points_)
		return []
	def Ys(self):
		if (len(self.points_) > 0):
			return map (lambda point: point.y(), self.points_)
		return []
		
class Engine:
	
	def __init__(self, A, B):
		self.A = A
		self.B = B
		self.fig = plt.figure()
		self.ax = self.fig.add_subplot(111)
		cid = self.fig.canvas.mpl_connect('button_press_event', self.onclick)
		cid = self.fig.canvas.mpl_connect('key_press_event', self.onkey)
		self.show_centers = False
		self.Draw()
		plt.show()
		
		
	def Draw(self):
		self.Ap, = self.ax.plot(self.A.Xs(), self.A.Ys(), 'ro',color = 'r')
		self.Bp, = self.ax.plot(self.B.Xs(), self.B.Ys(), 'r*',color = 'b')
		self.Ac,  = self.ax.plot([], self.B.Ys(),  'bo', color = 'g', markersize = 15)
		self.Bc,  = self.ax.plot([], self.B.Ys(), 'b*', color = 'g', markersize = 15)
		
	
	def redraw(self):
		self.Ap.set_xdata(self.A.Xs())
		self.Ap.set_ydata(self.A.Ys())
		self.Bp.set_xdata(self.B.Xs())
		self.Bp.set_ydata(self.B.Ys())
		if (self.show_centers):
			Ac = self.A.center()
			Bc = self.B.center()
			self.Ac.set_xdata([Ac.x()])
			self.Ac.set_ydata([Ac.y()])
			self.Bc.set_xdata([Bc.x()])
			self.Bc.set_ydata([Bc.y()])
			
		self.fig.canvas.draw()
	
	def onkey(self, event):
		n = 100
		if(event.key == " "):
			self.show_centers = not self.show_centers
		if(event.key == "r"):
			for point in map(lambda x, y: Point(x, y), np.random.rand(n), np.random.rand(n)):
				self.A.addPoint(point)
		if(event.key == "t"):
			for point in map(lambda x, y: Point(x, y), np.random.rand(n), np.random.rand(n)):
				self.B.addPoint(point)
		if(event.key == "y"):
			for point in map(lambda x, y: Point(x, y), np.random.rand(n), np.random.rand(n)):
				self.managePoint(point)
		self.redraw()
		
 	def onclick(self, event):
		p = Point(event.xdata, event.ydata)
		if(event.button == 1): #left
			self.A.addPoint(p)
		elif(event.button == 3): #right
			self.B.addPoint(p)
		elif(event.button == 2): #center
			self.managePoint(p)
		self.redraw()
		
	def managePoint(self, point):
		dA = self.A.center().distance(point)
		dB = self.B.center().distance(point)
		self.A.addPoint(point) if (dA < dB) else self.B.addPoint(point)
		
	def start(self, obj):
		obj.recalc()
		X,Y = obj.array()
		time.sleep(0.01)
		self.graphic.set_xdata(X)
		self.graphic.set_ydata(Y)
		plt.draw()

a = Cloud()
b = Cloud()
e = Engine(a,b)
