import random
import typing

def main():
    # print(f"isPalindrome('aba')={isPalindrome('aba)}")
    #  print(f"isPalindrome('aabaa')={isPalindrome('aabaa')}")
    #  print(f"isValidPalindrome('abca')={isValidPalindrome('abca')}")
     print(f"isValidPalindrome2('abcdccba')={isValidPalindrome2('abcdccba')}")
    #  print(f"isValidPalindrome2('aba')={isValidPalindrome2('aba')}")

# T=O(n) S=O(1)
def isValidPalindrome2(s: str)->bool:
    left, right = 0, len(s)-1
    while left < right:
        if s[left] != s[right]:
            return isPalindrome2(s,left+1,right) or isPalindrome2(s,left,right-1)
        left += 1
        right -= 1
    return True

def isPalindrome2(s: str, left: int, right: int)->bool:
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True 


# Brute force T=O(n*n) S=O(n)
def isPalindrome(s: str)->bool:
    left, right = 0, len(s)-1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def isValidPalindrome(s: str)->bool:
    for i in range(len(s)):
        sub_string = s[:i]+s[i+1:]
        if isPalindrome(sub_string):
            return True
    return isPalindrome(s)
# End Brute force

if __name__ == "__main__":
    main()

def generate_array(no_elements: int, min: int, max: int) -> list[int]:
    # Ensure that no_elements does not exceed the range of unique values available
    if no_elements > (max - min + 1):
        raise ValueError("The range is too small to generate the required number of unique values.")
    
    # Generate an array of unique random numbers
    random_array = random.sample(range(min, max + 1), no_elements)
    
    return random_array