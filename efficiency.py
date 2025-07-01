import threading
import time
from multiprocessing import Pool


def factorial(n):
        if n < 0:
            return None
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
def thread_worker(n, results, index):
    results[index] = factorial(n)

def threaded_factorial(numbers):
    threads = []
    results = [None] * len(numbers)
    for i, n in enumerate(numbers):
        t = threading.Thread(target=thread_worker, args=(n, results, i))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    return results

if __name__ == "__main__":
    numbers = [5, 18, 10, 15, 13, 16, 8]

    # Threading
    start = time.time()
    thread_results = threaded_factorial(numbers)
    end = time.time()
    print("Threading Results:", thread_results)
    print("Threading Time:", end - start)

    # Multiprocessing
    start = time.time()
    with Pool() as pool:
        multi_results = pool.map(factorial, numbers)
    end = time.time()
    print("Multiprocessing Results:", multi_results)
    print("Multiprocessing Time:", end - start)
    
    