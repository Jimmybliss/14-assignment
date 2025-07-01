import threading
import time
from multiprocessing import Pool

# Function to compute factorial of a number
def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Worker function for threading, stores result in the shared results list
def thread_worker(n, results, index):
    results[index] = factorial(n)

# Function to compute factorials using threads
def threaded_factorial(numbers):
    threads = []
    results = [None] * len(numbers)  # Shared list to store results
    for i, n in enumerate(numbers):
        # Create a thread for each number
        t = threading.Thread(target=thread_worker, args=(n, results, i))
        threads.append(t)
        t.start()  # Start the thread
    for t in threads:
        t.join()  # Wait for all threads to finish
    return results

if __name__ == "__main__":
    numbers = [5, 18, 10, 15, 13, 16, 8]  # List of numbers to compute factorial

    # Threading section
    start = time.time()  # Start timer
    thread_results = threaded_factorial(numbers)  # Compute using threads
    end = time.time()  # End timer
    print("Threading Results:", thread_results)
    print("Threading Time:", end - start)

    # Multiprocessing section
    start = time.time()  # Start timer
    with Pool() as pool:
        multi_results = pool.map(factorial, numbers)  # Compute using processes
    end = time.time()  # End timer
    print("Multiprocessing Results:", multi_results)
    print("Multiprocessing Time:", end - start)