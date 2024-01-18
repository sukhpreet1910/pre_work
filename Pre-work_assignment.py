"""Question 1
Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

    def hello_name(user_name):
        ....."""

def hello(user_name):
    print("Hello", user_name)

user_name = input("Enter Your Name: ")
hello(user_name)

    
"""              
Question 2
Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

    def first_odds():
        .....
"""

def first_odds():
    odds = []
    for i in range(101):
        if i % 2 != 0:
            odds.append(i)
    print(odds)

first_odds()


"""
Question 3
Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

    def max_num_in_list(a_list):
        .....
"""
def max_num_in_list(a_list):
    maxi = max(a_list)
    return maxi

a_list=[32, 1, -1, 45, 90]
max = max_num_in_list(a_list)

print("Maximum number is: ", max)




"""             
Question 4
Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

    def is_leap_year(a_year):
        .....
"""

def is_leap_year(a_year):
    if (a_year % 4 == 0 and a_year % 100 != 0) or (a_year % 400 == 0):
        return True
    else:
        return False
    
year = input("Enter the year you want to check: ")
try:
    year = int(year)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
result = is_leap_year(year)

if result:
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')


"""  
Question 5
Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

    def is_consecutive(a_list):
        ....."""

def is_consecutive(a_list):

    if len(a_list) < 2:
        return False
    
    sorted_list = sorted(a_list)
    return all((sorted_list[i] + 1) == sorted_list[i + 1] for i in range(len(sorted_list) - 1))
        

numbers1 = [2, 3, 4, 5, 6, 7]
numbers2 = [1, 2, 4, 5]

result1 = is_consecutive(numbers1)
result2 = is_consecutive(numbers2)

print(f"{numbers1}: {result1}")
print(f"{numbers2}: {result2}")




