def numbers():
    # Initialize an empty list to store three numbers
    threeNumbers = []
    
    # Initialize counters for positive and negative numbers
    negCount = 0
    posCount = 0

    # Loop to take input for three numbers
    for i in range(3):
        number = int(input("Enter your three numbers: "))
        threeNumbers.append(number)  # Append the entered number to the list
        if number > 0:
            posCount += 1  # Increment positive count if the number is positive
        elif number < 0:
            negCount += 1  # Increment negative count if the number is negative

    # Print the list of three numbers
    print(threeNumbers)

    # Check if exactly two numbers are positive and one is negative
    if posCount == 2 and negCount == 1:
        print(True)
    else:
        print(False)

# Call the function
numbers()
