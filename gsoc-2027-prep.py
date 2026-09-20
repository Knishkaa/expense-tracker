# ==========================================
# RECURSION DRILLS: Fundamentals & Tree Structures
# Author: Knishka
# ==========================================

##Q1. Write a function factorial(n) that returns the factorial of n using recursion (no loops).
def factorial (n):
     if n == 0 or n == 1:
         return 1
     else:
         return n * factorial(n-1)
 print(factorial(5))
## Q2. Write a recursive function sum_list(lst) that returns the sum of all numbers in a list.
def sum_list(lst):
     if len(lst)==1:
         return lst[0]
     else:
         return lst[0] + sum_list(lst[1:])
my_list=[1,5,6,7,8]
print(sum_list(my_list))
##Write a recursive function count_down(n) that prints numbers from n down to 1, then prints "Liftoff!".
def count_down(n):
     if n < 1:
         print("Liftoff!")
     else:
         print(n)
         count_down(n-1)
print(count_down(6))
##Write a recursive function fibonacci(n) that returns the nth Fibonacci number (0-indexed: fib(0)=0, fib(1)=1).
def fibonacci(n):
     if n <= 1:
         return n
     else:
         return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(8))
##Write a recursive function is_palindrome(s) that returns True if a string reads the same forwards and backwards, False otherwise. (No slicing shortcuts like s == s[::-1] — actually recurse.)
def is_palindrome(s):
     if len(s) <= 1:
         return True
     elif s[0] == s[-1]:
         return is_palindrome(s[1:-1])
     else:
         return False

print(is_palindrome("racecar"))
print(is_palindrome("hello"))
##Write a recursive function flatten(nested_list) that takes a nested list like [1, [2, 3, [4, 5]], 6] and returns a flat list [1, 2, 3, 4, 5, 6].
def flatten(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))  
        else:
            result.append(item)           
    return result

print(flatten([1, [2, 3, [4, 5]], 6])) 
##Write a recursive function count_elements(nested_list) that counts the total number of non-list elements in an arbitrarily nested list.
def count_elements(nested_list):
    count = 0
    for item in nested_list:
        if isinstance(item, list):
            count += count_elements(item)  
        else:
            count += 1                      

print(count_elements([1, [2, 3, [4, 5]], 6]))   
## Write a recursive function deep_sum(nested_list) that sums all numbers in an arbitrarily nested list (combine ideas from Q1-Q7).
def deep_sum(nested_list):
    total = 0
    for item in nested_list:
        if isinstance(item, list):
            total += deep_sum(item)
        elif isinstance(item, (int, float)):
            total += item
    return total

print(deep_sum([1, [2, 3, [4, 5]], 6]))   