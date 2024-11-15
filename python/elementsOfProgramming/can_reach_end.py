""" 
T = O(n)
S = O(1)
"""
import random

def main():
    a = generate_array(random.randint(2,5),0,3)
    print(f"A = {a}")
    furthest_reach_so_far, last_index = 0, len(a) - 1
    i = 0
    while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, a[i] + i)
        i += 1
    return furthest_reach_so_far >= last_index

def generate_array(no_elements: int, min: int, max: int) -> list[int]:
    # Ensure that no_elements does not exceed the range of unique values available
    if no_elements > (max - min + 1):
        raise ValueError("The range is too small to generate the required number of unique values.")
    
    # Generate an array of unique random numbers
    random_array = random.sample(range(min, max + 1), no_elements)
    
    return random_array

if __name__ == "__main__":
    main()
