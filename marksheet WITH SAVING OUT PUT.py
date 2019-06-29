
city = input("name of your city?(IN BOLD LETTERS) ")
group = input("GROUP ENGINEERING OR MEDICAL: ")
roll = input("enter your roll number: ")
name = input("enter your full name : ")
phy = input("enter your physics marks (less than 100): ")
chem = input("enter your chemistry marks (less than 100): ")
math = input("enter your math marks (less than 100): ")
urdu = input("enter your urdu marks (less than 100): ")
islam = input("enter your islamiat marks (less than 100): ")
total = 500
with open("whatever.txt", "w") as f:
    f.write("--------------------------------BOARD OF INTERMEDIATE EDUCATION " + city +"-------------------------------\n")

    f.write("GROUP: PRE "+group+"\n")
    f.write("ROLL NO: "+roll+"\n")
    f.write("NAME: "+name+"\n")
    f.write("---------------------------------------STATEMENT OF MARKS-------------------------------------------------\n")
    f.write("SUBJETS  OBTAIN MARKS TOTAL MARKS\n")
    f.write("PHYSICS:    "+ phy + "         100\n")
    f.write("CHEMISTRY:  "+ chem +"         100\n")
    f.write("MATH:       " + math+"         100\n")
    f.write("URDU:       "+ urdu +"         100\n")
    f.write("ISLAMIAT:   "+islam+ "         100\n")
    f.write("------------------------------------------------------------------------------------------------------------\n")


phy = int(phy)
chem = int(chem)
math = int(math)
urdu = int(urdu)
islam = int(islam)


#PERCENTAGE
obt = (phy+chem+math+urdu+islam)
percen = (obt/total)*100

obt = str(obt)
percen = str(percen)
#grade
with open("whatever.txt", "a") as f:
    f.write("OBTAIN MARKS:"+obt+"\n")
    f.write("PERCENTAGE:"+percen+"%\n")
    percen = float(percen)

    if percen >= 80:
       f.write("GRADE: 'A+'\n")
    elif percen >= 70 <80:
      f.write("GRADE: 'A'\n")
    elif percen >= 60 <70:
       f.write("GRADE: 'B'\n")
    elif percen >= 50 <60:
       f.write("GRADE: 'C'\n")
    elif percen >= 40 <50:
      f.write("GRADE: 'D'\n")
    else:
      f.write("GRADE: 'FAIL'")