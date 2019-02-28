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
# file = open("a_example.txt","r")
# inp = file.readlines()

# # n = int(input())


# # images = []
# # for i in range(n):
# # 	st = input().split()
# # 	li = []
# # 	for j in st[2:]:
# # 		li.append(j)
# # 	print(li)
images = []
images.append(image(0,3,{"cat","beach","sun"}))
images.append(image(1,2,{"selfie","smile"}))
images.append(image(1,2,{"selfie","garden"}))
images.append(image(0,2,{"garden","cat"}))

print(images)
print(bestOrder(images))
#print(images[2].calculateInterest(images[1]))


