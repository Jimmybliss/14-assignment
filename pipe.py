from multiprocessing import Process, Pipe

def worker(n, conn):
    # Compute factorial and send result through the pipe
    conn.send((n, factorial(n)))
    conn.close()

def master(numbers):
    processes = []
    parent_conns = []
    # Create a process and a pipe for each number
    for n in numbers:
        parent_conn, child_conn = Pipe()
        p = Process(target=worker, args=(n, child_conn))
        processes.append(p)
        parent_conns.append(parent_conn)
        p.start()

    # Collect results from all pipes
    results = [conn.recv() for conn in parent_conns]
    for p in processes:
        p.join()

    # Return only the factorial results, order may not match input
    # results.sort()  # Uncomment to sort by input order if needed
    return [res[1] for res in results]

if __name__ == "__main__":
    numbers = [5, 18, 10, 15, 13, 16, 8]
    pipe_results = master(numbers)
    print("Multiprocessing Pipe Results:", pipe_results)

def factorial(n):
    # Compute factorial of n, return None for negative numbers
    if n < 0:
        return None
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result