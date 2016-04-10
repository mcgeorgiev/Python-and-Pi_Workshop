# imports the random library
import random

print('This is a random number guessing game.')

# uses the random library's randrange method to get a number between 1 and 9
random_number = random.randrange(1,9)

# int() converts a string to an integer
guess = int(input('Please enter your guess: '))

# if random_number == guess:
#     print('You guessed right.')

# else:
#     print('You guessed wrong.')

# while loop. continues looping if condition is met.
# != means 'not equal to'
while guess != random_number:

    guess = int(input('You are incorrect.Please guess again: '))

print('You have guessed correctly.')
# str() converts the integer back to a string
print('The answer was ' + str(random_number))
