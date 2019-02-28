

class image:
	def __init__(self, orientation, number, tags):
		self.orientation = orientation
		self.number = number
		self.tags = tags

	def calculateInterest(self, image1):
		i1 = len( image1.tags - self.tags ) 
		i2 = len( image1.tags & self.tags )
		i3 = len( self.tags - image1.tags )
		return min(i1,i2,i3)

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
print(images[2].calculateInterest(images[1]))


