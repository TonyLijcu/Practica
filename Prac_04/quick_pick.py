numbers_per_line = 6
min = 1
max = 45

number_of_picks = int(input('How many quick picks? '))
while number_of_picks < 0:
    print("Pick a Positive number")
    number_of_picks = int(input('How many quick picks? '))

for