# Task 3
# Word Scramble

words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']

# Loop through each word (multiple indexes)
for word in words:
    scrambled = word[::-1]   # simple scramble

    print("\nScrambled word:", scrambled)

    while True:
        guess = input("Enter your guess: ").lower()

        if guess == word:
            print("Correct! Moving to next word...")
            break
        else:
            print("Wrong!le Try again.")



