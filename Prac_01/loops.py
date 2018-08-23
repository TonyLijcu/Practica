for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0,101,10):
    print(i,end=' ')
print()

for i in range(1,21,1):
    print((21-i),end=' ')
print()

Number_of_stars = int(input("Enter number of stars:"))
for i in range(Number_of_stars):
    print("*",end='')
print()

for i in range(0,Number_of_stars,1):
    print("*"*(i+1))
print()