# Filter creates a list of items for which the function returns true.
# list(filter(function))

ls = [2, 4, 5, 6, 8, 9]
a = filter(lambda x: x%2 == 0, ls)
print(list(a))
