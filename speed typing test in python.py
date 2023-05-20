import time
import random

def main():
    print("Welcome to Typing Master!")
    print("Type the given text as fast and accurately as you can.")
    print("Press ENTER when you're ready to start.")
    input()

    # The given text for typing test
    text = "The quick brown fox jumps over the lazy dog"
    words = text.split()

    # Shuffle the words to make the typing test more challenging
    random.shuffle(words)
    shuffled_text = " ".join(words)

    print(shuffled_text)
    input("Press ENTER to start the timer: ")
    start_time = time.time()

    # Get user input
    user_input = input()

    end_time = time.time()
    time_taken = end_time - start_time

    # Calculate typing speed and accuracy
    typed_words = user_input.split()
    correct_words = 0
    for i in range(len(typed_words)):
        if typed_words[i] == words[i]:
            correct_words += 1

    accuracy = (correct_words / len(words)) * 100
    typing_speed = (len(typed_words) / time_taken) * 60


    print(f"\nYou typed {len(typed_words)} words in {time_taken:.2f} seconds.")
    print(f"Your typing speed is {typing_speed:.2f} words per minute.")
    print(f"Your accuracy is {accuracy:.2f}%.")

if __name__ == "__main__":
    main()

