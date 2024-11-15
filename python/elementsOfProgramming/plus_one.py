""" 
T = O(n)
S = O(1)

Time complexity is O(n) where n is number elements in array
Space complexity is constant 
"""
import random

def main():
    a = generate_array(5,1,9)
    # a = [9,9,9]
    print(f"Generated Array = \n{a}")
    a[-1] += 1

    for i in reversed(range(1, len(a))):
        if a[i] != 10:
            break
        a[i] = 0
        a[i-1] += 1
    else:
        if a[0] == 10:
            a[0] = 1
            a.append(0)

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
