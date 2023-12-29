#This is a follow along project from tech with tim and can be found in the below link
#https://www.youtube.com/watch?v=21FnnGKSRZo&list=WL&index=10

#-------------------------------
import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input('enter the number of players (2-4):')
    
    #checks whether the input is a digit
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print('must be between 2-4')
    else:
        print('invalid, try again')

#f string syntax
print(f'This is the number of players: {players}')

max_score = 50

# gives a 0 for each player the notation is called a list comprehension
player_scores = [0 for i in range(players)]

# str.format() method in use
initialScores = 'This is the inital score list for the given players: {}'.format(player_scores)
print(initialScores)

#Continue while every player_score on the list is smaller than the maximum score
while max(player_scores) < max_score:

    #Loop through the players list to give each player their turn
    for player_id in range(players):
        print(f'''
              Player {player_id + 1} turn has just started!
              ''')
        current_score = 0

        while True:
            should_roll = input('Would you like to roll (y)?')
            if should_roll.lower() != 'y':#Formats the input into lower case
                break
            value = roll()
            if value == 1:
                print('You rolled a 1, turn done.')
                current_score = 0
                break
            else:
                current_score += value
                print(f'You rolled a {value}!')

            print('your current score is', current_score)

        player_scores[player_id] += current_score
        print(f'Your total score is: {player_scores[player_id]}')

max_score = max(player_scores)
#Find the index of the wanted value
winning_index = player_scores.index(max_score)

print(f'Player number {winning_index + 1} wins the game with a total of {max_score}')