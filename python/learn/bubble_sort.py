# T = O(n*n)
# S = O(1)

import random
import typing

def bubble_sort(a: list[int]) -> list[int]:
    for i in range(len(a)):
        swapped = False
        for j in range(len(a) - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
        if not swapped:
            break
    return a

def main():
    a = generate_array(5,1,9)
    # a = [9,9,9]
    print(f"Generated Array = \n{a}")
    
    a = bubble_sort(a)

    print(f"Final Array = \n{a}") 

def generate_array(no_elements: int, min: int, max: int) -> list[int]:
    # Ensure that no_elements does not exceed the range of unique values available
    if no_elements > (max - min + 1):
        raise ValueError("The range is too small to generate the required number of unique values.")
    
    # Generate an array of unique random numbers
    random_array = random.sample(range(min, max + 1), no_elements)
    
    return random_array

if __name__ == "__main__":
    main()
