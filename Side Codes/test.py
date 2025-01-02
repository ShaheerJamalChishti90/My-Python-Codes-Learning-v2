# numbers = range(3)
# output = {numbers}
# print(output)

data = [1, 2, 3]
output = {*data, *data}
print(output)