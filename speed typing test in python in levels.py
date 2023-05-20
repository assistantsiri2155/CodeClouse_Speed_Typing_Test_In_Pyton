import random
import time

# function to generate a random string of characters of given length
def generate_string(length):
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ()[]{};:,.<>/?'
    return ''.join(random.choice(characters) for i in range(length))

# function to calculate accuracy percentage
def calculate_accuracy(user_input, correct_input):
    correct_chars = 0
    for i in range(len(user_input)):
        if user_input[i] == correct_input[i]:
            correct_chars += 1
    return (correct_chars / len(correct_input)) * 100

# function to calculate words per minute speed
def calculate_speed(time_taken, correct_input):
    words = len(correct_input.split())
    speed = words / (time_taken / 60)
    return round(speed, 2)

# function to display the typing test results
def display_results(level, time_taken, correct_input, user_input):
    accuracy = calculate_accuracy(user_input, correct_input)
    speed = calculate_speed(time_taken, correct_input)
    print(f"Level {level} completed in {round(time_taken, 2)} seconds.")
    print(f"Accuracy: {accuracy}%")
    print(f"Speed: {speed} words per minute\n")

# function to run a typing test for a given level
def run_typing_test(level):
    # set the length and difficulty of the typing test based on the level
    if level == 1:
        length = 50
        difficulty = 'keyboard keys'
    elif level == 2:
        length = 75
        difficulty = 'small words'
    elif level == 3:
        length = 100
        difficulty = 'long words'
    elif level == 4:
        length = 3
        difficulty = 'lines'
    elif level == 5:
        length = 1
        difficulty = 'paragraph'
    else:
        print("Invalid level")
        return

    print(f"Level {level}: Type the following {difficulty} (press Enter when done):")

    # generate a random string of characters for the typing test
    correct_input = generate_string(length)
    print(correct_input)

    # start the timer
    start_time = time.time()

    # get the user input
    user_input = input()

    # stop the timer
    end_time = time.time()

    # display the results
    display_results(level, end_time - start_time, correct_input, user_input)

    # ask the user if they want to continue to the next level
    if level < 5:
        response = input("Do you want to continue to the next level? (y/n): ")
        if response.lower() == 'y':
            run_typing_test(level + 1)

# start the typing test at level 1
run_typing_test(1)

# display a congratulatory message when all levels are completed
print("Congratulations! You completed all the levels. Good job!")
