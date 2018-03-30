
from spy_details import spy_name,spy_age,spy_rating #importing a file with specific variables
print 'Hello' #greetings given to the user
print 'Let\'s get started' #initialising

def start_chat(spy_name,spy_age,spy_rating):#user define function created
    print 'Here are your options ' +spy_name#Message given to the user
    show_menu = True#by default value true for validation
    while show_menu:#using loop for multiple times show the same thing
        choice = input('What do you want to do ?\n1.Add a status\n2.Add a friend\n0.Exit ')#choices given to the userinput from the user
        if choice ==1:#conditional Statement
            print 'This will add the status of the spy'#Message for the user
        elif choice==2:#conditional Statement
            print 'This will add a friend' #Message for the user
        elif choice==0:#conditional Statement
            show_menu=False#Terminating the program
        else:#conditional Statement
            print 'Invalid option selected by you.!! '#Message for the user

spy_exist=raw_input('Are you an existing spy Y/N ')#asking the user whether he/she is an spy or not
if spy_exist.upper()=='Y':#conditional Statement
    print 'Welcome back %s age: %d having spy rating of %d' %(spy_name,spy_age,spy_rating)#Displaying the previous data for the user
    start_chat(spy_name,spy_age,spy_rating)#Calling  a  chat function
elif spy_exist.upper()=='N':#conditional Statement
    spy_name = raw_input('Enter Your Name ')#Message for the user and input from the user

    spy_rating=0.0#Initalising the variable
    spy_age=0#Initalising the variable
    if spy_name.isalpha():#Checking for name entered by the user as input
        spy_salutation = raw_input('What should we call you(Mr. or Ms.)')  # Message for the user and input from the user
        if len(spy_name)>=2 :#Checking the length of the name which should be greater than two
            if spy_salutation.upper()=='MR.' or spy_salutation.upper()=='MS.':#conditional Statement
                spy_name = spy_salutation.upper() + '' + spy_name.upper()#Concatinationg  2 string
                print 'Welcome '+spy_name +' Glad to have you back with us'##Concatinationg  2 string
                print 'Alright '+spy_name+'. '+'I\'d like to know a little bit more about you ...'#Concatinationg  2 string
                spy_age=input('what is your age ')#input taken from the user
                if 50>spy_age>12:#conditional statement
                    print 'You are eligible for being spy '+str(spy_age)#concationating th integer with the string
                    spy_rating=input('Please enter your rating ')#input from the user
                    if spy_rating>5.0:#Conditional statement
                        print'You are Expert in Spying.You have been assigned a task'#Message given to the user
                    elif 3.5<spy_rating<=5.0:#Conditional statement
                        print 'You are Goood in Spying. You will be assigned a task. Soon'#Message given to the user
                    elif 2.5<spy_rating<=3.5:#Conditional statement
                        print 'You are not a Spy But Still You are in Queue'#Message given to the user
                    else:#Conditional statement
                        print 'Who hired You? You are fired!!!'#Message given to the user
                    spy_is_online = True#Initialising the variable
                    print 'Authentication Complete.Welcome ' +spy_name+ ' age: ' +str(spy_age)+' and rating is '+str(spy_rating) # Concatinating two integer with a string
                    start_chat(spy_name, spy_age, spy_rating)#calling a  chat function

                else:#Conditional statement
                    print 'You should grow up till now!! Common man'#Message to the user
            else:#Conditional statement
                print 'Wrong Salutation'#Message to the user
        else:#Conditional statement
            print 'Enter a valid name'#Message to the user
    else:#conditional Statement
        print 'invalid name'

else:#Conditional statement
    print 'Inavalid Option.Please try next time'#Message to the user