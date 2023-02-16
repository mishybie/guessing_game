#This program demonstrates a gueesing game
#game
from random import randint


# 1 get user input  
user_name=input("whats your name?")
print("Hello there" +user_name +"!")

#generate a random number
random_number=randint(10,50)



counter=0
while counter <5:
    user_number=eval(input("Enter a random number:"))
    counter += 1

    if user_number<random_number:
      print("Your guess is too low.")
    elif user_number >random_number:
      print("Your guess is too high.")
    elif user_number==random_number:
      print("you win!")
    break



print("Game over:")

if user_number== random_number:
    print("You win!")
else:
    print("Game over!The correct number is")
    print(random_number)


# 2 generate a random number
#get user number

# 3 using a while loop
#check if user input is equal to generated number


