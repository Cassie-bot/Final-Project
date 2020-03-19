#Casandra Villagran
#3/4/2020

#The story is about a boy/girl who has lost their memory and is searching for their family at the same time.
#But in order to do so they must go through the spooky woods.

#Chapter 4

import time

print("CHAPTER 4")

#If/else statment
time.sleep(1)
print("Are you ready to get started? ")
answer=input()
if answer== "yes":
    print("Great let's go!")
else:
    print("I think you meant yes... No worries!")
time.sleep(1)
print("Background: After you heard realized which way the noise was coming from you headed that direction.")
time.sleep(6)
print("Present day: While heading down that path you see a crowd of people run down the same path you’re on with tons of lanterns screaming someone’s name...")
time.sleep(6)
i = "yes"
while i:
    i =input("Do you want to walk up to them? (Type: 'yes' or 'no') ")
    if i== "yes":
        print("Yayy, that might be your family!")
        print("TO BE CONTINUED...")
        break
    elif i== "no":
        print("The pack of wolves found you! (You died)")
        break
    else:
        print("This in an invalid answer. Try again!")

