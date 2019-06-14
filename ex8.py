"""If the marks obtained by a student in five different subjects
are input through the keyboard, find out the aggregate marks
and percentage marks obtained by the student. Assume that
the maximum marks that can be obtained by a student in each
subject is 100.
"""

s1 = int(input("Enter marks of subject one"))
s2 = int(input("Enter marks subject two "))
s3 = int(input("Enter marks subject three"))
s4 = int(input("Enter marks subject four"))
s5 = int(input("Enter marks subject five"))

avg=(s1+s2+s3+s4+s5)/500
per = (avg) *100

print(avg,per)
