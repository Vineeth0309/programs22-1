import time
print("Press ENTER to start the stopwatch")
print("and, press CTRL + v to stop the stopwatch")
while True:
    try:
        input()  # For ENTER
        start_time = time.time()
        print("Stopwatch started...")
    except KeyboardInterrupt:
        print("Stopwatch stopped...")
        end_time = time.time()
        print("The total time:", round(end_time - start_time, 2), "seconds")
        break