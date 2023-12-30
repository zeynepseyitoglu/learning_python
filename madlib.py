#This is a follow along code from tech with tim
#https://www.youtube.com/watch?v=21FnnGKSRZo&t=1420s
#-------------------------------------------

#With...as.. is a context manager that ensure the file properly closes after reading
with open('story.txt', 'r') as file:
    story = file.read()

words = set()
start_of_word = -1

target_start = '['
target_end = ']'

#The enumerate function returns pairs of indices and values
for index, char in enumerate(story):
    if char == target_start:
        start_of_word = index

    if char == target_end and start_of_word != -1:
        word = story[start_of_word : index + 1]
        words.add(word)
        start_of_word = -1

answers = {}

for word in words:
    answer = input('Enter a word for ' + word + ':')
    answers[word] = answer

for word in words:
    #str.replace replaces all instances of the found substring with the given string
    story = story.replace(word, answers[word])

print(story)