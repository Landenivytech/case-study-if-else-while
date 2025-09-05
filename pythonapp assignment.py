#Landen Tillman
#pythonapp assignment.py
#This app calculates if you have made honor roll or made the Deans list or nothing at all
while True:
    
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
