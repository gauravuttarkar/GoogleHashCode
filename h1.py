class image:
	def __init__(self, orientation, number, tags):
		self.orientation = orientation
		self.number = number
		self.tags = tags

	def calculateInterest(self, image1):
		print(type(image1))
		print(image1)
		i1 = len( image1.tags - self.tags ) 
		i2 = len( image1.tags & self.tags )
		i3 = len( self.tags - image1.tags )
		return min(i1,i2,i3)


def bestOrder(images):
	if ( len(images) <= 2 ):
		return [ [images[0], images[1]], images[0].calculateInterest(images[1])]
	interestFactor = 0
	m = 0
	order = None
	for i in range(len(images)):
		be = bestOrder(images[:i]+images[i+1:])
		print(type(be[0][-1]))
		if ( images[0].calculateInterest(be[0][0]) <  
			images[0].calculateInterest(be[0][-1])):
			if images[0].calculateInterest(be[0][-1]) + be[1] > m:
				m = images[0].calculateInterest(be[0][-1]) + be[1]
				order = be[0].append([images[0]])
			return [ be[0].append([images[0]]), 
					images[0].calculateInterest(be[0][-1]) + be[1] ]
		else:
			if images[0].calculateInterest(be[0][0]) + be[1] > m:
				m = images[0].calculateInterest(be[0][0]) + be[1]
				order = [images[0]] + be[0]
			return [[images[0]] + be[0], 
					images[0].calculateInterest(be[0][0]) + be[1] ]

	return order
	
file = open("a_example.txt","r")
inp = file.readline()

n = inp
print(n)

data = file.readlines()
data = [d[:-1] for d in data]

images = []
for i in range(len(data)):
	st = data[i].split()
	if(st[0] == "H"):
		st[0] = 0
	else:
		st[0] = 1
	print(st[0],st[1],st[2:])
	images.append(image(st[0],st[1],st[2:]))

print(images)
print(bestOrder(images))
#print(images[2].calculateInterest(images[1]))


