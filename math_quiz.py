import random
import time

OPERATOR = ['+', '-', '*']
MAX_OPERAND = 20
MIN_OPERAND = 3
TOTAL_PROBLEMS = 10

def generate_problem():
    #Gives a random integer between the provided values
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    #chooses a random value from the provided list
    operator = random.choice(OPERATOR)

    expression = str(left) + ' ' + operator + ' ' + str(right)
    #Used to evaluate a string as a python expression
    answer = eval(expression)
    return expression, answer

wrong= 0
input('''
      Press enter to start!
      ---------------------
      ''')

# gives the current time in seconds
start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expression, answer = generate_problem()
    while True:
        guess = input(f'Problem #{str(i + 1)}: {expression} = ')
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time() 
total_time = end_time - start_time

print(f'''
      Nice work! yout total time is {round(total_time, 2)}
      ------------------------------------------ ''')