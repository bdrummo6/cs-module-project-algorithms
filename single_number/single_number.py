# MVP 1
"""
Input: a List of integers where every int except one shows up twice
Returns: an integer
"""
# Time complexity: O(n)
# Space complexity: O(1)
def single_number(arr):
    # set single to the first element in the list
    single_num = arr[0]

    # Loop through the list starting at the second element
    for i in range(1, len(arr)):
        # Using the XOR bitwise operator check which element only appears once in the list
        single_num ^= arr[i]

    return single_num


if __name__ == '__main__':
    # Use the main function to test your implementation
    list_1 = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(list_1)}")