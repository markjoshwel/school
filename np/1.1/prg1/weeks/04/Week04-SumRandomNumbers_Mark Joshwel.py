# SumRandomNumbers
#   Mark Joshwel, SXXXXXXXX
# ================
# Quizzes user on sum of two random numbers from (0-100 inclusive)

from random import randint

rand1 = randint(0, 100)
rand2 = randint(0, 100)
if int(input(f"Enter the sum of {rand1} and {rand2}: ")) != (rand1 + rand2):
    print("Your answer is wrong.\n" f"The correct answer is {rand1 + rand2}.")
else:
    print("Your answer is correct.")
