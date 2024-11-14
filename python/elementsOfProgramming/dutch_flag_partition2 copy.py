""" 
T = O(n)
S = O(1)

Time complexity is O(n) where n is number elements in array
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
smaller = 0
for i in range(len(a)):
    if a[i]<pivot:
        a[smaller], a[i] = a[i], a[smaller]
        smaller += 1

print(f"Array after moving same elements on right =\n {a}")

# bigger to right
larger = len(a) - 1
for i in reversed(range(len(a))):
    if a[i] > pivot:
        a[larger], a[i] = a[i], a[larger]
        larger -= 1

print(f"Array after bigger number on right=\n{a}")
