# MVP 2
"""
Input: a List of integers
Returns: a List of integers
"""
# Time complexity: O(n)
# Space complexity: O(1)
def moving_zeroes(arr):
    count = 0

    # This loop moves all non-zero values to the front of the list
    for i in range(len(arr)):
        # if a value at the current index does not equal zero store value at index count
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1  # increment count by 1

    # Loop through the rest of the list adding the zeros to the end
    while count < len(arr):
        arr[count] = 0
        count += 1

    return arr  # return the mutated array with all 0s at the end

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    list_1 = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(list_1)}")