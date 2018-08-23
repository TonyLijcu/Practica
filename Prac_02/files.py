name = input('Your name:')
out_file = open('name.txt', 'w')
print(name, file=out_file)
out_file.close()

in_file = open('name.txt', 'r')
name = in_file.read().strip()
print('your name is', name)
in_file.close()

in_file = open('number.txt', 'r')
number = int(in_file.readline())
number1 = int(in_file.readline())
print(number + number1)
in_file.close()

print("version 2")
in_file = open('number.txt', 'r')
sum = 0
for line in in_file:
     sum += int(line)
print(sum)
in_file.close()
