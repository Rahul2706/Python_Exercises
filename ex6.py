#Ramesh’s basic salary is input through the keyboard.

bs = int(input("Enter basic salary of ramesh : "))

#dearness allowance is 40% of basic salary
da = bs * 0.4
#allowance is 20% of basic salary
al = bs * 0.2
#Gross Salary??

gs = bs - da - al

print("Gross salary of ramesh :", gs)