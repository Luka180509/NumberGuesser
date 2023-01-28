import time as t

Max_Num = eval(input('Please Pick any number above 2:'))
if Max_Num > 2:
    t.sleep(1)
    print(f'now pick number from 0 to {Max_Num} included 0 and {Max_Num}')
    t.sleep(5)
    print('alright')
    t.sleep(1)

    Longness = 0
    x = []
    y = 0
    Guessed_Num = 0
    List = 1
    Add = 1

    #Checks for maximum posibility for n in x^n
    
    for SUM in range(Max_Num):
        if Longness == 0:
            if 2**SUM > Max_Num:
                Longness = SUM

    for Long in range(Longness):
        #makes a list
        y = Add-1
        for i in range(round(Max_Num/2)):
            for Z in range(Add):
                if not y > Max_Num:
                    y += 1
                    if not y > Max_Num:
                        x.append(y)
            for Z in range(Add):
                if not y > Max_Num:
                    y += 1

        #seperates list from other list
        
        for junk in range(3):
            print('')
        print(f'_______________________________LIST {List}_______________________________')
        print(x)
        YN = input('is the number that you picked in the following list? (0 for no, 1 for yes)')
        
        #Checks if you said yes or no and adds the first number of the list to variable
        
        if int(YN) == 1:
            Guessed_Num += Add


        #clears the list, getting ready for next list
        
        y = Add-1
        for i in range(round(Max_Num/2)):
            for Z in range(Add):
                if not y > Max_Num:
                    y += 1
                    if not y > Max_Num:
                        x.remove(y)
            for Z in range(Add):
                if not y > Max_Num:
                    y += 1

        #checks for what number should be added to the variable when said yes next time
        
        if Add == 1:
            Add += 1
        else:
            Add = Add * 2

        List += 1

    #and finally tells you your picked number
    
    for junk in range(3):
            print('')
    print(f'Your picked number is {Guessed_Num}')
else:
    #if maximum number was not above 2 give you a warn message
    print('i said above 2!')
