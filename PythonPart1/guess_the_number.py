'''
secret_number = 5
print("I am thinking of a number between 1 and 10.")
while True:
    total = input("What is the number? ")
    if total != '5':
        print("Nope, try again. ")
    else:
        print("Yes! You Win! ")
        break

#Step 2
secret_number = 5
print("I am thinking of a number between 1 and 10.")
while True:
    total = input("What is the number? ")
    if total > '5':
        print(total + "  is too high")
    elif total < '5':
        print(total + " is too low")
    else:
        print("Yes! You Win! ")
        break
'''
#step 3
import random
my_random_number = random.randint(1, 10)
print("I am thinking of a number between 1 and 10.")
tries = 5
while True:
    total = int(input("What is the number? "))
    print("you have" ,tries, "guesses left.")
    if total > my_random_number:
        tries=tries-1
        print(total ,"  is too high")
    elif total < my_random_number:
        print(total , " is too low")
        tries=tries-1
    else:
        print("Yes! You Win! ")
        break
    if tries==0:
        print("you lose the number is",my_random_number)
        break

