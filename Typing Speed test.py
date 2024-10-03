import random
import datetime

#--------------------------------Functions--------------------------------------
def begin():
    global name
    global lines
    print('''\n-------------------------------------------
Welcome To Typing Test Project
Please input the number according to your choice-
Type "1" if you are using this program for the first time.
Type "2" if you have used this program before.
-------------------------------------------\n''')
    user = input('Your input: ')

    if user == '1':
        name = input('\nPlease enter your name: ')
        create(name)
        print('''\n-------------------------------------------
Please input the number according to your choice-
Type "1" if you want to start the test.
Type "2" if you want to exit the program.
-------------------------------------------\n''')
        ans = input('Your input: ')
        
        if ans == '1':
            print('''\n-------------------------------------------
IMPORTANT GUIDELINES
1.The test will have 4-5 lines maximum. The more you attempt the more accurate the results would be.
2.If you want to end the test, input ONLY "break" and it'll immediately terminate the test and display the result.
-------------------------------------------\n''')
            input('Press any key to continue.\n')
            start(lines)
        elif ans == '2':
            return
        
        else:
            print('Please select a proper option.')
    elif user == '2':
        name = input('\nPlease enter your name: ')
    	try:
            check1(name)
            print('''\n-------------------------------------------
Please input the number according to your choice-
Type "1" if you want to view details of the previous tests.
Type "2" if you want to start the test.
-------------------------------------------\n''')
            choice = input('Your input: ')            
            if choice == '1':
                fetch(name)
            elif choice == '2':
                print('''\n-------------------------------------------
IMPORTANT GUIDELINES
1.The test will have 4-5 lines maximum. The more you attempt the more accurate the results would be.
2.If you want to end the test, input ONLY "break" and it'll immediately terminate the test and display the result.
-------------------------------------------\n''')
                input('Press any key to continue.\n')
                start(lines)                
            else:
                print('Please select a proper option.')
                begin()                
        except:
            print(f'No file with name "{name}" was found.\n')
            print('''-------------------------------------------
Please input the number according to your choice-
Type "1" if you want to add your name to our database.
Type "2" if you want to return to the main menu.
Type "3" if you want to exit the program.
-------------------------------------------\n''')
            ans = input('Your input: ')
            if ans == '1':
                create(name)
                begin()
            elif ans == '2':
                begin()
            elif ans == '3':
                return
            else:
                print('Please select a proper option.')
                begin()                
    else:
        print('Please select a proper option.')
        begin()
    
def check1(name):
    open(f'.\\Users\\{name}.txt' , 'r')

def fetch(name):
    info = open(f'.\\Users\\{name}.txt' , 'r')
    a = info.read()
    print('\n')
    if a == '':
        print('No data currently stored.')
    else:
        print(a)
    info.close()    

def create(name):
    try:
        open(f'.\\Users\\{name}.txt' , 'r')
        print(f'\nA file with name {name} already exists.\n\n')
        begin()
    except:
        open(f'.\\Users\\{name}.txt' , 'w')
        print(f'\nFile created with name: {name}\n\n')

def start(lines):
    global original
    global check    
    i = 0
    z = 0
    sent = ''
    tim = open(f'.\Time\\time.txt' , 'w')
    a = datetime.datetime.now()
    tim.write(str(a))
    tim.close()
    
    for line in lines:
        word = line.split()
        
        for i in range (len(word)):

            try:
                for y in range (z*10,(z*10)+10):
                    if y == ((z*10)+9):
                        sent += f'{word[y]}'
                    else:
                        sent += f'{word[y]} '
                    y += 1
                    

                print(sent)
                z+= 1
                for h in list(sent):
                    original.append(h)                        
                sent = ''             

            except IndexError:
                break
            
            sentence = input()
            if sentence == 'break':
                break
            for u in list(sentence):
                check.append(u)   
                    
        i += 1

    result(original,check)
def result(original,check):
    global name
    tim1 = open(f'.\Time\\time.txt' , 'r')
    tim2 = tim1.read()
    tim3 = datetime.datetime.strptime(tim2, '%Y-%m-%d %H:%M:%S.%f')    
    tim1.close()    
    time1 = datetime.datetime.now()
    time = time1 - tim3
    
    a = time.total_seconds()
    b = round(a/60,2)

    for x in range (0,len(original)):
        try:
            if original[x] == check[x]:
                correct.append(original[x])
        except IndexError:
            break
            
                    
    wpm = round(((len(correct))/5)/b,2)
    accuracy = round(((len(correct))/len(original)) * 100,2)
    print(f'Accuracy: {accuracy}%')
    print(f'WPM: {wpm}')
    save(accuracy,wpm,name,time1)

def save(accuracy,wpm,name,time1):
    a = open(f'.\\Users\\{name}.txt' , 'a')
    date = time1.date()
    sec = datetime.datetime.strftime(time1,'%d %b %Y, %A, %H:%M:%S')
    text = f'Test started at: {sec}\nAccuracy: {accuracy}%\nWPM (word per minute): {wpm}\n\n'
    a.write(text)
    a.close()





#----------------------------Main Program----------------------------


stories = ["Story1","Story2","Story3","Story4","Story5","Story6"]
choice = random.choice(stories)

story = open(f'.\Stories\{choice}.txt' , 'r')
lines = story.readlines()

original = []
check = []
correct = []
begin()
