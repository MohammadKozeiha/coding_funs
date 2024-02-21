import threading
import time

# Define a function that will be executed by each thread
def task():
    print("Thread {} is running...".format(threading.current_thread().name))
    time.sleep(2)
    print("Thread {} is finished.".format(threading.current_thread().name))

# Create multiple threads
threads = []
for i in range(5):
    thread = threading.Thread(target=task)
    thread.start()
    threads.append(thread)

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All threads have finished.")
