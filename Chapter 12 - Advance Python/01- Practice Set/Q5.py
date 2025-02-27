# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt

x = int(input("Enter the number: "))

# table = [x*i for i in range(1, 11)]


# with open("myfriendmimi.txt", "a") as f:
#     f.write(str(table))
#     f.write("\n")
#     print("The tables have been written successfully.")


with open("Mimi_Tables.txt", "a") as f:
    for i in range(1, 11):
        f.write(f"{x} x {i} = {x*i}\n")
    print("The tables have been written successfully.")