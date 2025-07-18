def bubble_sort(list):
    n = len(list)
    for i in range(n):
        # Loop through the listay from 0 to n-i-1
        for j in range(0, n - i - 1):
            # Swap if the current element is greater than the next
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

# # Example usage
# numbers = [64, 34, 25, 12, 22, 11, 90]
# print("Original list:", numbers)

# bubble_sort(numbers)

# print("Sorted list:", numbers)

# numbers = [64, 34, 25, 12, 22, 11, 90]
# print(numbers.sort())
# print(sorted(numbers))
