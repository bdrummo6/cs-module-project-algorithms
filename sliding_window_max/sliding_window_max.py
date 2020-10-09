# MVP 4
"""
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
"""
def sliding_window_max(nums, k):
    max_nums = []

    i = 0
    while i < len(nums) - k + 1:
        window_size = i + k
        max_nums.append(max(nums[i:window_size]))
        i += 1

    return max_nums


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    size = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, size)}")
