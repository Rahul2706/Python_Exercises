"""Temperature of a city in Fahrenheit degrees is input through
the keyboard. Write a program to convert this temperature
into Centigrade degrees.
"""

Fahrenheit = int(input("Enter temp. in Fahrenheit : ")) #(32°F − 32) × 5/9 = 0°C

Centigrade = (Fahrenheit - 32)*(5/9) 

print(Centigrade)