from typing import List

def main():
    # arr = [4, 5, 6, 7, 0, 1, 2, 3]
    arr = [0, 1, 2, 3, 4, 5, 6, 7] 
    result = search(arr, 7)  # Pass both the array and the target
    print(result)

def search(nums: List[int], target: int) -> int:
    n = len(nums)
    l = 0
    r = n - 1

    # Find the index of the smallest element (rotation point)
    while l < r:
        m = (l + r) // 2
        if nums[m] < nums[r]:
            r = m
        else:
            l = m + 1

    rotation = l
    l = 0
    r = n - 1

    # Perform binary search adjusted for the rotation
    while l <= r:
        m = (l + r) // 2
        real_mid = (m + rotation) % n
        if nums[real_mid] == target:
            return real_mid
        elif nums[real_mid] < target:
            l = m + 1
        else:
            r = m - 1

    return -1

if __name__ == "__main__":
    main()