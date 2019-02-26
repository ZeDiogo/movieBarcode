import numpy as np
import cv2
from Image import Image

def smooth(colors):
	avgColor = [0, 0, 0] ## TODO
	counter = 0
	for color in colors:
		# if np.all(color == 0):
		# 	continue
		# if color == [0,0,0]:
		# 	continue
		# else:
		counter += 1
		avgColor[0] += color[0]
		avgColor[1] += color[1]
		avgColor[2] += color[2]

	print avgColor[0]
	print avgColor[1]
	print avgColor[2]
	avgColor[0] = avgColor[0] / counter
	avgColor[1] = avgColor[1] / counter
	avgColor[2] = avgColor[2] / counter
	
	print counter
	newColumn = []
	for i in range(counter):
		newColumn.append(avgColor)
	return newColumn



def main():
	# EDIT----------
	columnPercentage = 30 # percentage
	filename = 'atlantida.mkv'
	framesToInclude = 1000
	# --------------


	cap = cv2.VideoCapture(filename)
	ret, frame = cap.read()
	width = frame.shape[1]
	height = frame.shape[0]
	columnPosition = columnPercentage * width / 100
	img = Image(width, height)
	numberFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
	frameRate = numberFrames / float(framesToInclude)
	print 'number frames', numberFrames
	loop = 0

	while(cap.isOpened()):
	# for i in range(0.0, framesToInclude):
		
		col = []
		ret, frame = cap.read()
		if (loop % frameRate) < 1:
			if not ret:
				break
			print '1'
			cv2.imshow('frame',frame)
			for line in frame:
				colorR = int(line[columnPosition][0])
				colorG = int(line[columnPosition][1])
				colorB = int(line[columnPosition][2])
				color = [colorR, colorG, colorB]
				col.append(color)
			img.addColumn(smooth(col))

			# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			# print frame[height-1][width-1]

			if cv2.waitKey(1) & 0xFF == ord('q'):
				break
		# if loop > 1000:
		# 	break
		loop += 1
		print loop, '/', numberFrames
	print 'end'
	img.printSize()
	cv2.imwrite('frame.png', img.getImage())
	cap.release()
	cv2.destroyAllWindows()

if __name__ == '__main__':
	main()