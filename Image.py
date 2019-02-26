import numpy as np

class Image:

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.img = [ [] for i in range(self.height) ]
		# self.img = np.zeros((self.height,self.width,3), np.uint8)

	def addColumn(self, array):
		if len(array) != self.height:
			print 'Error column doesnt has the same dimension'
			print 'Image has height = ' + str(self.height)
			print 'column has height = ' + str(len(array))
		for i, color in enumerate(array):
			self.img[i].append(color)

	def printSize(self):
		print 'Image dimension: ', len(self.img[0]), 'x', len(self.img)

	def getImage(self):
		return np.array(self.img)

