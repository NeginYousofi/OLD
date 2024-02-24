# Exercise 1:

# Write a program that will ask the user to enter three numbers and then return the sum
"""
number1 = float(input("Please enter the firt number: "))
number2 = float(input("Please enter second number: "))
number3 = float(input("Please enter a number: "))
sum = (number1 + number2 + number3)
print(sum) 
"""

# Exercise 2: Ask the user to input 2 numbers and then perform the following mathematical operation
# on those two numbers: +, -, *, /, %, //, **. For each operation print out the operation name and
# the result.
"""
n1 = float(input("enter the first number: "))
n2 = float(input("enter the second number: "))
#sum = (n1 + n2)
#print(sum)
# minos = ( n1 - n2 )
# print(minos)
# mul = (n1 * n2)
# # print(mul)
# div = ( n1 / n2)
# print(div)
# ex = (n1 ** n2)
# print(ex)
# fd = (n1 // n2)
# print(fd)
# mod = (n1 % n2)
# print(mod)
"""

# Exercise 3: What will be the result of the following python operations?
# 0 / 4
# 4 / 0
"""
n1 = 0
n2 = 4
nn = (n1 / n2)
print(nn)
"""
# Exercise 4: Correct these lines of code using type conversion. Then print the calculated result
# of all three variables and their data type.



# price_3_books = float('5.0') * 3
# print(price_3_books)
# my_age = str('I am ') + "26"
# print(my_age)
# total_bill = 4.45 + 3.30 + 6 + float('7')
# print(total_bill)

# # Exercise 5:
# Suppose your teacher wants to calculate your average grade, based on three grades that it gave
# you for an assignment. Ask the user three times to input a number (assignment grade, convert the
# input to the correct data type and assign them to variables. Calculate and print the average of
# the three numbers. Provide your code with useful comments.

n1 = float(input("Please enter the first number: "))
n2 = float(input("Please enter the second number: "))
n3 = float(input("Please enter the third number: "))
average = (n1 + n2 + n3)
print(f"The average is: {average}")