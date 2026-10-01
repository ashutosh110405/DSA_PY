"""
5. Reverse the Array: Write a program to accept N integers into an array and display the
elements in reverse order without changing the original array.
"""
n = int(input("Enter the number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

print("Original array:", arr)
print("Reversed array:", arr[::-1])