#Casandra Villagran
#3/4/2020

#The story is about a boy/girl who has lost their memory and is searching for their family at the same time.
#But in order to do so they must go through the spooky woods.

import time

#Chapter 1
print("CHAPTER 1")
name= input("Hello, Welome! What is your name? ")
print ("Nice to meet you " + name)
time.sleep(1)

#While Loop
i = "yes"
while i:
    i =input("Are you ready to get this adventure started? ")
    if i == "yes":
        print("Great, Let's get started!")
        #User is ready to play!      
        time.sleep(1)
        print("Background: Today is Monday, it's been a month since you last seen your family. You fell into a ditch and were lucky to survive, but sadly you lost your memory.")
        time.sleep(10)
        print("Present day: It was a dark fogy night in the woods and there was no one to be seen, but an old man on a rocking chair.")
        time.sleep(10)
        print(name + " if you talk to the man you might get some information on where your family is.")
        #The user will have the option to ask the man for help which leads to getting a map that will get user through the woods
        #Or the user doesn't have to talk to the man, but he wont have a map to help him in the woods
        time.sleep(1)
        answer= input("Want to talk to him? Type 'yes' or 'no' ")
        if answer== "yes":
            print("Great, let's go")
            print("TO BE CONTINUED...")
            break
        elif answer== "no":
            print("To late he is walking your way!")
            print("TO BE CONTINUED...")
            break
        else:
            print("Invalid, but no worries! I know you wanted to talk to him!")
            print("TO BE CONTINUED...")
            break
    elif i == "no":
        print(name + " I think you meant yes! Try again!")
        #User is not ready to play
    else:
        print(name + " this in an invalid answer. Try again!")
        
