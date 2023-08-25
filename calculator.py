# a = '5'
# b = '6'
# enterNumberOne = input('enter first number: ')
# enterNumberTwo = input('enter Second number: ')
# # input()
# c = int(enterNumberOne) + int(enterNumberTwo)
# print(c)

# DEVELOPMENT OF FULL CALCULATOR BELOW - 17/08/2023:
# We will use the following concepts below:
# variable
# operators
# if and else
# function

# EXPECTED FUNCTIONALITIES FOR CALCULATOR BELOW:
# 1. Addition
# 2. Subtraction
# 3. Division
# 4. Multiplication
# METHOD OF CALCULATION
# NUMBER NUMBER & OPERATOR, OR
# NUMBER OPERATOR & NUMBER *
# OPERATOR NUMBER & NUMBER

def my_calculator():
    integer_one = input(' Please enter the first integer:  ')
    operator = input('Please enter an operator sign or name: ')
    integer_two = input(' Please enter the second integer:  ')

    # ADDITION
    if operator == 'add' or operator == '+' or operator == 'ADD' or operator == 'aDD' or operator == 'plus' or operator == 'Add':
        result = int(integer_one) + int(integer_two)
        print(result)

    # SUBTRACTION
    elif operator == 'minus' or operator == '-' or operator == 'subtract' or operator == 'remove':
        result = int(integer_one) - int(integer_two)
        print(result)

    # DIVISION
    elif operator == 'divide' or operator == '/':
        result = int(int(integer_one) / int(integer_two))
        print(result)

    # MULTIPLICATION
    elif operator == 'multiply' or operator == '*':
        result = int(integer_one) * int(integer_two)
        print(result)

    else:
        print('You entered a wrong operator. Please use a correct one.')


my_calculator()
