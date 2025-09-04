#Landen Tillman
#pythonapp assignment.py
#This app calculates if you have made honor roll or made the Deans list or noth,king at all
while True:
    gpa = float(input("your GPA: "))
    name = input("your name: ")
    last_name = input("your last name: ")
    if last_name == 'ZZZ':
        print('exit')
        break
    if gpa >= 3.5:
        print(name + ' you have made the Dean List.')
    elif gpa >= 3.25:
        print(name + ' you have made Honor Roll.')
    else:
        print('You did not make honor roll or the deans list.')
# your GPA: 3.20
# your name: landen
# your last name: till
# You did not make honor roll or the deans list.
# your GPA: 3.9
# your name: landej
# your last name: timsb
# landej you have made the Dean List.
# your GPA: 3.7
# your name: alnde
# your last name: ZZZ