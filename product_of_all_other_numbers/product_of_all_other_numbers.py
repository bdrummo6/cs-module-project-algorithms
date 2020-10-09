# MVP 3
"""
Input: a List of integers
Returns: a List of integers
"""
def product_of_all_other_numbers(arr):
    elements = len(arr)

    # Base case
    if elements == 1:
        return [0]

    # Allocate memory for temporary arrays left[] and right[]
    left = [0] * elements
    right = [0] * elements

    # Allocate memory for the product array
    product = [0] * elements

    # Left most element of left array is always 1
    left[0] = 1

    # Rightmost most element of right array is always 1
    right[elements - 1] = 1

    # Construct the left array
    for i in range(1, elements):
        left[i] = arr[i - 1] * left[i - 1]

        # Construct the right array
    for j in range(elements - 2, -1, -1):
        right[j] = arr[j + 1] * right[j + 1]

    # Construct the product array using
    # left[] and right[]
    for i in range(elements):
        product[i] = left[i] * right[i]

    return product


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    list_1 = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(list_1)}")
