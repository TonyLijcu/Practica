Number = []
for i in range(5):
    number = int(input("Write a number: "))
    Number.append(number)

print("The first number is", Number[0])
print("The last number is", Number[-1])
print("The smallest number is", min(Number))
print("The largest number is", max(Number))
print("The average of the numbers is", sum(Number) / len(Number))