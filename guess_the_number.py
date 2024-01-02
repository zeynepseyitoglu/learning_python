import random

number_range = int(input('Give me an upper limit!\n'))
number = random.randint(1, number_range)

while True:
    guess = input('Guess! \n')
    if guess.isdigit():
        if int(guess) == number:
            print('You got it!')
            break
        if int(guess) > number:
            print('Try smaller.')

        if int(guess) < number:
            print('Go bigger.')
    else:
        print('Please enter a number.')
