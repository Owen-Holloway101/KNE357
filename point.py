class point:
	X = 0
	Y = 0
	Z = 0
	R = 0

	def __init__(self,x,y,z,r):
		self.X = x
		self.Y = y
		self.Z = z
		self.R = r

	def printPoint(self):
		print("X: %i Y: %i Z: %i R: %i" % (self.X, self.Y, self.Z, self.R))
