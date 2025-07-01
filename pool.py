from multiprocessing import Pool

def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    numbers = [5, 18, 10, 15, 13, 16, 8]
    with Pool() as pool:
        results = pool.map(factorial, numbers)
    print("Multiprocessing Pool Results:", results)
