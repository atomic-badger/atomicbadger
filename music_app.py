#This program is used to structure a beginner's music practice.
#program calls text functions and uses input requests
#program execution is linear


# creates opening greeting
def lets_play():
    print("\n**********************************************************\n")
    print("Welcome to the Linux Music Practice App.\n")
    print("**********************************************************\n")
    print("\n**********************************************************\n")
    print("\nWelcome to the music practice app.\n")
    play_status = input("Do you wish to play music today? \n\tPlease enter yes or no.\t")
    if (play_status != "yes"):
        print("\nYou have chosen no.\n")
        print("\nHave a nice day.\n")
        quit()
    else:
        print("\nExcellent. Let's practice.\n")
        print("\n**********************************************************\n")


# choose instrument
def inst_choice():
    print("\n**********************************************************\n")
    print("\nYou have three instruments available to choose from.\n")
    print("\nA:    Guitar\n")
    print("\nB:    Piano\n")
    print("\nC:    Synthesizer\n")
    inst_1=input("\nWhat instrument do you choose? Please spell out the answer.\t")
    print("\n\tYou have chosen " + inst_1 +".\t\n") 
    print("\n**********************************************************\n")     
    

#C Major scale
def practice_one():
    print("\n**********************************************************\n")
    print("\nLet's begin by practicing a C Major scale.\n")
    print("The notes are C,D,E,F,G,A,and B.")
    print("\tYou do have to know these notes to practice this scale.\n")
    status_2=input("Please enter yes when you have completed the C Major scale.\t")
    if(status_2 != "yes"):
        print("\n\tWaiting until complete.\n")
        input("\tPlease enter yes when you have completed the C Major scale.\t")
    else:
        print("\nExcellent. We will go on to the next scale.\n")
        print("\n**********************************************************\n")


# F Major scale
def practice_two():
    print("\n**********************************************************\n")
    print("\nLet's practice an F Major Scale.\n")
    print("The notes are F,G,A,Bb,C,D, and E.")
    print("\tYou do have to know these notes to practice this scale.\n")
    status_3=input("Please enter yes when you have completed the F Major scale.\t")
    if(status_3 != "yes"):
        print("\n\tWaiting until complete.\n")
        input("\tPlease enter yes when you have completed the F Major scale.\t")
    else:
        print("\nExcellent. We will go on to the next scale.\n")
        print("\n**********************************************************\n")


#G Major Scale
def practice_three():
    print("\n**********************************************************\n")
    print("\nLet's practice a G Major Scale.\n")
    print("The notes are G,A,B,C,D,E and F#.")
    print("\tYou do have to know these notes to practice this scale.\n")
    status_4=input("Please enter yes when you have completed the G Major scale.\t")
    if(status_4 != "yes"):
        print("\n\tWaiting until complete.\n")
        input("\tPlease enter yes when you have completed the G Major scale.\t")
    else:
        print("\nExcellent. We will go on to the next scale.")
        print("\n**********************************************************\n")


#A minor scale
def practice_four():
    print("\n**********************************************************\n")
    print("\nLet's practice an A minor Scale.\n")
    print("The notes are A,B,C,D,E,F, and G.")
    print("\tYou do have to know these notes to practice this scale.\n")
    status_5=input("Please enter yes when you have completed the A minor scale.\t")
    if(status_5 != "yes"):
        print("\n\tWaiting until complete.\n")
        input("\tPlease enter yes when you have completed the A minor scale.\t")
    else:
        print("\nExcellent. Your practice today is complete.\n")
        print("\nHave a wonderful day.")
        print("\n**********************************************************\n")
        print("\n**********************************************************\n")
 

 #run functions
lets_play()
inst_choice()
practice_one()
practice_two()
practice_three()
practice_four()
quit()
#end of functions
