# marksheet.md
city = input("name of your city?(IN BOLD LETTERS) ")
group = input("GROUP ENGINEERING OR MEDICAL: ")
roll = input("enter your roll number: ")
name = input("enter your full name : ")
phy = int(input("enter your physics marks (less than 100): "))
chem = int(input("enter your chemistry marks (less than 100): "))
math = int(input("enter your math marks (less than 100): "))
urdu = int(input("enter your urdu marks (less than 100): "))
islam = int(input("enter your islamiat marks (less than 100): "))
total = 500




print("--------------------------------BOARD OF INTERMEDIATE EDUCATION " + city +"----------------------------------")

print("GROUP: PRE "+group)
print("ROLL NO: "+roll)
print("NAME: "+name)
print("---------------------------------------STATEMENT OF MARKS-----------------------------------------------------")
print("SUBJETS       OBTAIN MARKS          TOTAL MARKS")
print("PHYSICS:       ", phy, "                   100")
print("CHEMISTRY:     ", chem, "                   100")
print("MATH:          ", math, "                   100")
print("URDU:          ", urdu, "                   100")
print("ISLAMIAT:      ", islam, "                   100")
print("--------------------------------------------------------------------------------------------------------------")

#PERCENTAGE
obt = (phy+chem+math+urdu+islam)
print("TOTAL OBTAIN MARKS: ", obt)
percen = (obt/total)*100
print("PERCENTAGE:", percen, "%")

#grade
if percen >= 80:
    print("GRADE: 'A+'")
elif percen >= 70 <80:
    print("GRADE: 'A'")
elif percen >= 60 <70:
    print("GRADE: 'B'")
elif percen >= 50 <60:
    print("GRADE: 'C'")
elif percen >= 40 <50:
    print("GRADE: 'D'")
else:
    print("GRADE: 'FAIL'")
