"""
https://www.codewars.com/kata/563cf89eb4747c5fb100001bhat are left.
"""
#Solution
def remove_smallest(arr):
    if not arr:
        return []

    min_value = min(arr)
    new_arr = arr[:]
    new_arr.remove(min_value)

    return new_arr

# Example usage:
original_array = [4, 2, 5, 1, 3]
result_array = remove_smallest(original_array)
print("Original Array:", original_array)
print("Result Array:", result_array)

