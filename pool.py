from multiprocessing import Pool  # Import Pool class for parallel processing

def factorial(n):
    # Calculate the factorial of a non-negative integer n
    if n < 0:
        return None  # Return None for negative inputs
    result = 1
    for i in range(2, n + 1):
        result *= i  # Multiply result by each number from 2 to n
    return result

if __name__ == "__main__":
    numbers = [5, 18, 10, 15, 13, 16, 8]  # List of numbers to compute factorials for
    # Create a pool of worker processes
    with Pool() as pool:
        # Map the factorial function to each number in the list using the pool
        results = pool.map(factorial, numbers)
    # Print the results from the multiprocessing pool
    print("Multiprocessing Pool Results:", results)
