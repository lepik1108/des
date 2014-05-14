import numpy as np

class OBJ:
	engine_ = None
	
	def setEngine(self, engine):
		self.engine_ = engine
	
	def recalc():
		pass_
	
	def array():
		return None

class Bal(OBJ):
	
	def __init__(self, x, y, velocity = 0, mass = 3,
				 g = 9.8, k1 = 1, k2 = 1,
				 dt = 1, n = 10):
		self.x_ = x
		self.y_ = y
		self.velocity_ = velocity
		self.g_ = g
		self.k1_ = k1
		self.k2_ = k2
		self.mass_ = mass
		self.n_ = n
		self.i_ = 0
		self.dt_ = dt
		print ("Start x y = (",x,",",y,")")
		print ("Start velocity = (", velocity)
		print ("Start mass = (", mass)
		print ("g = (", g)
		print ("dt = (", dt)
		
		
		
	def array(self):
		X = [self.x_]
		Y = [self.x_]
		return X,Y
		
	def stop(self):
		self.i_ = 0 
			
	def recalc(self):
		print self.i_, self.velocity_
		self.i_ += 1
		new_v = (self.mass_ * self.g_ - self.velocity_ - self.velocity_**2)
		new_v = new_v / self.mass_
		new_v *= self.dt_
		self.velocity_ = new_v
		if(self.i_ > self.n_):
			self.stop()
		
