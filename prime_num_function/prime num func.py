
  # *************************************
# Tam Fredrick Kofi
# Date: 21/09/2014
# file: kofi.py
# UNI: fkt2105 
#
#***************************************

# question 4

# Python program to check if the input number is prime or not

# take input from the user
num = int(input("Enter a number: "))

# prime numbers are greater than 1
if num > 1 and num <10*10**6:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
       
# if input number is less than
# or equal to 1 or greater than 10 million, it is not prime
else:
   print(num,"is not a prime number or may not be in range of calculation")

