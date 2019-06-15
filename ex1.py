"""
Question :-1 Write a C program to read the age of a candidate and determine 
whether it is eligible for casting his/her own vote
"""

age = int(input("Enter age of  a person : "))

if age>18 :
	print("Eligible for vote")
else:
	print("Not Eligible for vote")