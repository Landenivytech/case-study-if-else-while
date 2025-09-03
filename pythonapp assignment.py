#Landen Tillman
#pythonapp assignment.py
#This app calculates if you have made honor roll or made the Deans list or noth,king at all
GPA = float(input("your GPA: "))
name = input("your name: ")
last_name = input("your last name: ")
if GPA >= 3.5:
    print(name + ' you have made the Dean List.')
if GPA >= 3.25:
    print(name + ' you have made Honor Roll')
