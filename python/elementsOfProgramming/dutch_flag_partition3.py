""" 
T = O(n)
S = O(1)

Time complexity is O(n) where n is number elements in array
Space complexity is constant 
"""
import random

def main():
    a = generate_array(10,1,100)
    print(f"Generated Array = \n{a}")
    smaller, equal, larger, pivot = 0, 0, len(a), a[4]
    print(f"Pivot = {pivot} \n")

    while equal < larger:
        if a[equal] < pivot:
            a[smaller], a[equal] = a[equal], a[smaller]
            smaller, equal = smaller + 1, equal + 1
        elif a[equal] == pivot:
            equal = equal + 1
        elif a[equal] > pivot:
            larger -= 1
            a[larger], a[equal] = a[equal], a[larger]
    print(f"Final Array::\n {a}")

def generate_array(no_elements: int, min: int, max: int) -> list[int]:
    # Ensure that no_elements does not exceed the range of unique values available
    if no_elements > (max - min + 1):
        raise ValueError("The range is too small to generate the required number of unique values.")
    
    # Generate an array of unique random numbers
    random_array = random.sample(range(min, max + 1), no_elements)
    
    return random_array

if __name__ == "__main__":
    main()
