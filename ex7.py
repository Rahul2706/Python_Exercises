"""
The distance between two cities (in km.) is input through the
keyboard. Write a program to convert and print this distance
in meters, feet, inches and centimeters.
"""
km = int(input("Enter distance b/w two cities in km : "))

meter = km*1000

cm = km*100000

feet = km*3280.84

inches = km*39370.1

print( "Distances b/w two cities are :" , meter , cm , feet , inches )






