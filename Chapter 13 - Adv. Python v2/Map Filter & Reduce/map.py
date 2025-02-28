# Map applies a function to all the items in an input_list
# map(function, input_list)


ls = [2, 4, 6, 8]

a = map(lambda x: x*x, ls)
print(tuple(a))