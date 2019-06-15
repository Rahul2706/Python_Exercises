x=int(input("Enter  points of x  axis :")) #problem
y=int(input("Enter  points of y axis :"))

if x==0 & y!=0:
	print("point is on x-axis")
else:
	if x!=0 & y==0:
		print("Point is on the y-axis")
	else:
		print("Point is on origin")