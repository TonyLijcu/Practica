Min_Length = 2
Max_Length = 6
Special_Chars_Required = True
Special_Chars = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    print("Please enter a valid password")
    print("Your password must be between", Min_Length, "and", Max_Length, "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if Special_Chars_Required:
        print("\tand 1 or more special characters: ", Special_Chars)
    Password = input('> ')
    while not is_valid_password(Password):
        print('Invalid Password')
        Password = input('> ')
    print("Your " + str(len(Password)) + " character password is valid: " + Password)


def is_valid_password(Password):
    if len(Password) < Min_Length or len(Password) > Max_Length:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in Password:
        if char.isdigit():
            count_digit += 1
        elif char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char in Special_Chars:
            count_special += 1

    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False

    if Special_Chars_Required:
        if count_special == 0:
            return False
    return True


main()
