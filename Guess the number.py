# Task 3
# Guess the Number

low = 1
high = 50

print("Think of a number between 1 and 100")

while low <= high:
    mid = (low + high) // 2
    print("Is your number:", mid)

    feedback = input("Enter 'h' (high number), 'l' (low number), 'c' (correct): ").lower()

    if feedback == 'c':
        print("Yay! I guessed it!")
        break
    elif feedback == 'h':
        high = mid - 1
    elif feedback == 'l':
        low = mid + 1
    else:
        print("Invalid input!")


