import random

numbers_per_line = 6
min = 1
max = 45

number_of_picks = int(input('How many quick picks? '))
while number_of_picks < 0:
    print("Pick a Positive number")
    number_of_picks = int(input('How many quick picks? '))

for i in range(number_of_picks):
    picks = []
    for j in range(numbers_per_line):
        number = random.randint(min,max)
        if number in picks:
            number = random.randint(min, max)
        picks.append(number)
        picks.sort()
    print(picks)


