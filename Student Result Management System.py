print("-"*10 + " Welcome to Student Result Management System " + "-"*10)
Name=input("Enter Student Name: ")
Roll_No=input("Enter Roll Number: ")
sub=input("Enter Subject no: ")
marks=[]
total=0
for i in range (int(sub)):
    mark=int(input("Enter you maarks:{}: ".format(i+1)))
    marks.append(mark)
    

for j in marks:
    total+=j
average=total/int(sub)
if average>=90:
    grade="A+" 
elif average>=80:
    grade="A"
elif average>=70:
    grade="B"
elif average>=60:
    grade="C"
elif average>=50:
    grade="D"    
else:
    grade="F"

print("Student name:",Name)
print("Roll Number:",Roll_No)
print("Total Marks:",total)
print("Average Marks:",average)
print("Grade:",grade)
print("-"*10 + " Thank you for using Student Result Management System " + "-"*10)