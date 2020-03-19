#Casandra Villagran
#3/4/2020

#The story is about a boy/girl who has lost their memory and is searching for their family at the same time.
#But in order to do so they must go through the spooky woods.

#Chapter 3
import time

print("CHAPTER 3")

#If/else statment
time.sleep(1)
print("Are you ready to get started? ")
answer=input()
if answer== "yes":
    print("Great, let's go!")
else:
    print("I think you meant yes... No worries!")
time.sleep(1)
print("Background: After you spoke to the little girl she pointed to the wide path ahead of you!")
time.sleep(3)
print("Present day: It gets louder as you walk deeper in the woods as if there are people on the other side.")
time.sleep(5)
i = "yes"
while i:
    i =input("Do you want to stop and listen to where the noise is coming from? ")
    if i == "yes":
        print("Great, That might be where your family is, listen closely!")
        print("TO BE CONTINUED...")
        break
    elif i == "no":
        print("OH NO, You walked into a tribe of wolves! (You died)")
        break
    else:
        print("This in an invalid answer. Try again!")
