import random

print("Welcome to Number Guessing\n Don't Hesitate to follow me on Github : Jimichelle\n")
#Start With Lower and Upper Ranges
print("Select your lower then upper range of guessing :")
lower_number = input("Lower Number : ")
upper_number = input("Upper Number : ")
print("Your range of guessing is between " + lower_number + " and " + upper_number)
random_number = random.randint(int(lower_number),int(upper_number))
number_guess = int(input("How much guessing you need ? : "))
print("You choose %d guessing\n" % number_guess)
count = 0
print("The Game is starting \n")
while count <= number_guess:
    guess = int(input("Your Guess : "))
    if guess == random_number:
        print("You WON")
        break
    else:
        count +=1
        print("Try Again")
