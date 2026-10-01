"""
#1. Calculate Array Sum: Write a program to accept N integers
#into an array and calculate and display the sum of all the elements.
"""

n = int(input("Enter the number of elements in the array: "))
arr = []

for i in range(n):
    num = int(input(f"Enter element {i + 1}: "))
    arr.append(num)

total_sum = sum(arr)
print(f"The sum of all elements in the array is: {total_sum}")