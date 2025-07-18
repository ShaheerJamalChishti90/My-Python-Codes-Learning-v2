def calculate_the_sum(a, b, c):
    return f"The sum of {a}, {b} and {c} is {a + b + c}"
    
def main():
    print(f"This is the result of 1st Function: {calculate_the_sum(5, 5, 5)}")
    x = lambda a, b, c : a + b + c
    print(x(5, 6, 7))
main()