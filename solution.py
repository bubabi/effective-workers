import heapq


# n workers (n is odd), workers work as pair, cost is abs difference of pair
# calculate total min cost
# example 1 input: 4 2 8 1 9
# min cost: |2-1| + |8-9| = 2
# example 2 input: 4 1 2 16 8
# min cost: |2-1| + |8-4| = 5
def calculate_min_cost(workers):
    workers.sort()
    workers_idx = set()
    min_heap = []
    min_cost = 0

    for i in range(len(workers) - 1):
        heapq.heappush(min_heap, (abs(workers[i] - workers[i + 1]), (i, i + 1)))

    while len(min_heap):
        min_diff = heapq.heappop(min_heap)
        cost = min_diff[0]
        worker_a, worker_b = min_diff[1][0], min_diff[1][1]
        if not (worker_a in workers_idx or worker_b in workers_idx):
            workers_idx.add(worker_a)
            workers_idx.add(worker_b)
            min_cost += cost

    return min_cost


if __name__ == '__main__':
    # workers = [4, 2, 8, 1, 9] # returns 2 true
    # workers = [4, 1, 2, 16, 8]  # returns 5 true
    workers = [2, 4, 5, 6, 9]  # returns 4 false
    calculate_min_cost(workers)
