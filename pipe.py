from multiprocessing import Process, Pipe

def worker(n, conn):
    conn.send((n, factorial(n)))
    conn.close()

def master(numbers):
    processes = []
    parent_conns = []
    for n in numbers:
        parent_conn, child_conn = Pipe()
        p = Process(target=worker, args=(n, child_conn))
        processes.append(p)
        parent_conns.append(parent_conn)
        p.start()

    results = [conn.recv() for conn in parent_conns]
    for p in processes:
        p.join()

    # sort to match original order
    # results.sort()
    return [res[1] for res in results]

if __name__ == "__main__":
    numbers = [5, 18, 10, 15, 13, 16, 8]
    pipe_results = master(numbers)
    print("Multiprocessing Pipe Results:", pipe_results)


def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result