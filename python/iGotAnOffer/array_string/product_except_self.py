import random
from typing import List  # Import List for type hints

def main():
    a = generate_array_with_duplicate(1,4,4)
    print(f"Array Input={a}")
    print(f"Output={product_except_self(a)}")


def product_except_self(nums):
    n = len(nums)
    output = [1] * n  # Initialize the output array with 1s

    # First pass: Calculate the prefix product for each element
    prefix = 1
    for i in range(n):
        output[i] = prefix
        prefix *= nums[i]

    # Second pass: Multiply with the suffix product
    suffix = 1
    for i in range(n - 1, -1, -1):
        output[i] *= suffix
        suffix *= nums[i]

    return output

def generate_array_with_unique(min_value: int, max_value: int, no_of_elements: int )-> List[int]:
    if(no_of_elements > (max_value - min_value + 1)):
        raise ValueError("Number of elements is greater than difference max and min values")
    return random.sample(range( min_value, max_value + 1), no_of_elements)

def generate_array_with_duplicate(min_value: int, max_value: int, no_of_elements: int) -> List[int]:
    return random.choices(range( min_value, max_value + 1), k=no_of_elements)

if __name__ == "__main__":
    main()
