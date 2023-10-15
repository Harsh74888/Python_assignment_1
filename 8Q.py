# find the sum of digit of an integer using while loop 
n=int(input("enter a number"))
sum_of_digit=0
while n > 0:
    digit = n % 10
    sum_of_digit += digit
    n //= 10
    print("The sum of digits is:", sum_of_digit)

