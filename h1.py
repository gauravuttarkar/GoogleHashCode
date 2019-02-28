class image:
	def __init__(self, orientation, number, tags):
		self.orientation = orientation
		self.number = number
		self.tags = tags

	def calculateInterest(self, image1):
		#print(type(image1))
		#print(image1)
		i1 = len( image1.tags - self.tags ) 
		i2 = len( image1.tags & self.tags )
		i3 = len( self.tags - image1.tags )
		return min(i1,i2,i3)


def bestOrder(images):
	if ( len(images) <= 2 ):
		return [ [images[0], images[1]], images[0].calculateInterest(images[1])]
	interestFactor = 0
	m = 0
	
	for i in range(len(images)):
		be = bestOrder(images[:i]+images[i+1:])
		print(be)
		#print(type(be[0][-1]))
		if ( images[0].calculateInterest(be[0][0]) <  
			images[0].calculateInterest(be[0][-1])):
			print("1")
			if images[0].calculateInterest(be[0][-1]) + be[1] > m:
				print("if")
				print(type(be[0]),be[0])
				m = images[0].calculateInterest(be[0][-1]) + be[1]
				print(type(images[0]),images[0])
				order = be[0] + [images[0]]
				print(order)
				print(m, order)
			return [ be[0] + [images[0]], 
					images[0].calculateInterest(be[0][-1]) + be[1] ]
		else:
			print("2")
			if images[0].calculateInterest(be[0][0]) + be[1] > m:
				m = images[0].calculateInterest(be[0][0]) + be[1]
				print("Inside else")
				print(type(be[0]))
				print("**")
				print([images[0]]+be[0])
				print("**")
				order = [images[0]] + be[0]
				print(m, order)
			return [[images[0]] + be[0], 
					images[0].calculateInterest(be[0][0]) + be[1] ]

	return order

images = []
images.append(image(0,3,{"cat","beach","sun"}))
images.append(image(1,2,{"selfie","smile"}))
images.append(image(1,2,{"selfie","garden"}))
images.append(image(0,2,{"garden","cat"}))

print(images)
order = bestOrder(images)

for i in order[0]:
	print(i.tags)
#print(images[2].calculateInterest(images[1]))


