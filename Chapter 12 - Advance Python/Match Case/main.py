x = int(input("Enter your age here: "))

match x:
    case _ if x < 15:
        print("You are not eligible to watch the movies in this theater.")

    case 15:
        print("You are eligible to watch these movies: 123")

    case 20:
        print("You are eligible to watch these movies: 123, 456")
        
    case 25:
        print("You are eligible to watch these movies: 123, 456, 789")
    
    case _ if x > 25:
        print("You are eligible to watch all the movies.")