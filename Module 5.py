#Casandra Villagran
#3/4/2020

#The story is about a boy/girl who has lost their memory and is searching for their family at the same time.
#But in order to do so they must go through the spooky woods.

#Chapter 5

import time

print("CHAPTER 5")
time.sleep(1)

#While Loop
x = 0
i = "yes"
while i:
    i =input("Are you ready to get started? ")
    if i == "yes":
        print("Great, Let's go!")
        #User is ready to play!      
        time.sleep(1)
        print("Background: After you walked up to the crowd of people they looked at you in shock.")
        time.sleep(4)
        print("Present day: A little girl and boy run from the crowd to hug you with excitement.")
        time.sleep(3)
        print("Do you want to ask who they are?")
        answer= input("(Type: 'yes' or 'no') ")
        if answer == "yes":
            print("You: Who are you guys?")
            time.sleep(2)
            print("Them: We're your family silly! We're so happy that we found you! We need to get you to the hospital!")
            time.sleep(4)
            print("You found your family! THE END!")
            time.sleep(2)
            while x < 100:
                print("You won")
                x += 1
                
            #Game ended and user is reunited with family
        elif answer == "no":
            print("You lost your chance of reuniting with your family! Now you got united with the wolves... (You died)")
            time.sleep(2)
            while x < 100:
                print("You lost")
                x += 1 
               
    elif i == "no":
        print("I think you meant yes, no worries! Try again!")
        #User is not ready to play
    else:
        print("This in an invalid answer. Try again!")
        
    break
