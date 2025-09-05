#Landen Tillman
#pythonapp assignment.py
#This app calculates if you have made honor roll or made the Deans list or nothing at all
while True:
    #imso sorry about the wait on my assignments I have been trying to get them setup at home.
    last_name = input("your last name: ")
    if last_name == 'ZZZ':
        print('exit')
        break
    gpa = float(input("your GPA: "))
    name = input("your name: ")
    
    if gpa >= 3.5:
        print(name + ' you have made the Dean List.')
    elif gpa >= 3.25:
        print(name + ' you have made Honor Roll.')
    else:
        
        print('You did not make honor roll or the deans list.')
        #FIX TESTING
# your last name: tillman
# your GPA: 3.6
# your name: landen
# landen you have made the Dean List.
# your last name: illman
# your GPA: 3.20
# your name: anden
# You did not make honor roll or the deans list.
# your last name: llman
# your GPA: -2
# your name: land
# You did not make honor roll or the deans list.
# your last name: sill
# your GPA: 5.0
# your name: bill
# bill you have made the Dean List.
# your last name: ZZZ
# exit
