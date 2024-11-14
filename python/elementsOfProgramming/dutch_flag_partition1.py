"""
Brute force method 
T = O(n*n)
S = O(1)

Time complexity is n*n becasue in worst case senario when all the elements 
before pivot are greater
after pivot are smaller

Space complexity is constant 
"""

import random

# generate an array from random numbers between 1 and 100
a = []
num_of_element = 10
min_element=1
max_element=100
a = random.sample(range(min_element,max_element+1),num_of_element)
print(f"Output of Array =\n {a}")

# Dutch flag partition brute form method

pivot = a[4]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[j]<pivot:
            a[i], a[j] = a[j], a[i]
            break

print(f"Array after moving same elements on right =\n {a}")

# bigger to right
for i in reversed(range(len(a))):
    for j in reversed(range(i)):
        if a[j] > pivot:
            a[i], a[j] = a[j], a[i]
            break

print(f"Array after bigger number on right=\n{a}")
