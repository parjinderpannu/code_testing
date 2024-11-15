""" 
T = O(n)
S = O(1)
"""
import random

def main():
    a = generate_array(random.randint(2,2),1,9)
    b = generate_array(random.randint(2,2),1,9) 
    # a[0] = -a[0]
    print(f"A = {a} \n B = {b}")
    sign = -1 if (a[0]<0) ^ (b[0]<0) else 1
    a[0] , b [0] = abs(a[0]), abs(b[0])

    result = [0]* (len(a)+len(b))

    for i in reversed(range(len(a))):
        for j in reversed(range(len(b))):
            result[i+j+1] += a[i] * b[j]
            result[i+j] += result[i+j+1] // 10
            result[i+j+1] %= 10

    result = result[next(( i for i, x in enumerate(result) 
                          if x != 0), len(result)):] or [0]
    print(f"****************\nresult={result}") 

def generate_array(no_elements: int, min: int, max: int) -> list[int]:
    # Ensure that no_elements does not exceed the range of unique values available
    if no_elements > (max - min + 1):
        raise ValueError("The range is too small to generate the required number of unique values.")
    
    # Generate an array of unique random numbers
    random_array = random.sample(range(min, max + 1), no_elements)
    
    return random_array

if __name__ == "__main__":
    main()
