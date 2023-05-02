import time

def typing_speed_test():
    print("Welcome to the Speed Typing Test!")
    time.sleep(1)
    print("Type the following sentence as fast as you can:\n")

    sentence = "The quick brown fox jumps over the lazy dog."
    print(sentence)

    start_time = time.time()
    user_input = input("> ")
    end_time = time.time()

    time_taken = end_time - start_time
    words_typed = len(user_input.split())
    speed = words_typed / time_taken * 60

    print(f"\nTime taken: {time_taken:.2f} seconds")
    print(f"Words typed: {words_typed}")
    print(f"Speed: {speed:.2f} words per minute")

typing_speed_test()
