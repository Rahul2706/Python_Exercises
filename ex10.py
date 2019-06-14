"""
The length & breadth of a rectangle and radius of a circle are
input through the keyboard. Write a program to calculate the
area & perimeter of the rectangle, and the area &
circumference of the circle.
"""

l = int(input("Enter lenght rectangle"))
b = int(input("Enter breadth rectangle"))
r = int(input("Enter radius of a circle"))

aor = (l*b)
perimeter = l+l+b+b 
aoc= 3.14* r**2
coc= 2*3.14*r

print(aor,aoc,perimeter,coc)