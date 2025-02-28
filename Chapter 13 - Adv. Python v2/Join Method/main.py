# "".join(object) method is used to join the elements of the object with the string as a separator.
# It returns the concatenated string.
# The join() method takes an iterable - objects capable of returning its members one at a time.
# Some examples of iterables are strings, lists, tuples, and dictionaries.
# The join() method does not change the original string, it returns a new string.
# The separator is the string that is used to join the elements of the object.
# If the separator is not specified, the elements are joined with no spaces.
# If the separator is an empty string, the elements are joined without any separator.
# If the separator is None, the elements are joined with no separator.


# Example 1: Joining List of Strings
# List of strings
numList = ['1', '2', '3', '4']
# numList = [1, 2, 3, 4, 5]
# Join all the strings in list
# using join() method
seperator = ', '
print(seperator.join(numList))