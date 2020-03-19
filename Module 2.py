#Casandra Villagran
#3/4/2020

#The story is about a boy/girl who has lost their memory and is searching for their family at the same time.
#But in order to do so they must go through the spooky woods.

#Chapter 2

import time

print("CHAPTER 2")

#If/else statment
time.sleep(1)
print("Are you ready to get started? ")
answer=input()
if answer== "yes":
    print("Great, let's go!")
else:
    print("I think you meant yes... No worries!")
time.sleep(1) 
print("Background: After you spoke to the man, he gave you a map!")
print("+1 Map added to player")
time.sleep(4)
print("Present day: While using the guidance of the map you go deeper into the woods, which became scarier and scarier. As the wind blew harder and harder it caused you to lose the map the old man gave you.")
time.sleep(10)
print("Oh no!")
time.sleep(1)
print("-1 map")
time.sleep(1)
print("A little girl is coming your way and it looks as if she has blood coming out of her eyes!")
time.sleep(6)
print("If you talk to the little girl she could know where to go next. Want to talk to her?")
answer=input()
if answer== "yes":
    print("Great, Let's go! She's only 5 steps away...")
    time.sleep(1)
    #For Loop
    #Prints out the numbers 0,1,2,3,4,5
    for x in range(6):
        print(x)
        time.sleep(1)
    print("TO BE CONTINUED...")
elif answer== "no":
    print("To late... She's walking your way! She's only 5 steps away...")
    time.sleep(1)
    #For Loop
    # Prints out the numbers 0,1,2,3,4,5
    for x in range(6):
        print(x)
        time.sleep(1)
    print("TO BE CONTINUED...")
else:
    print("This in an invalid answer. But she's coming your way! She's only 5 steps away...")
    time.sleep(1)
    #For Loop
    # Prints out the numbers 0,1,2,3,4,5
    for x in range(6):
        print(x)
        time.sleep(1)
    print("TO BE CONTINUED...")
