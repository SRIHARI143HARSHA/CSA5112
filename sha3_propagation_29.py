import random, statistics

T, C, R = 25, 9, 16        # total lanes, capacity lanes, rate lanes

def trial():
    cap = set(range(C))    # lanes 0..8 are the original capacity lanes
    hit = set()
    blocks = 0
    while len(hit) < C:
        blocks += 1
        active = set(random.sample(range(T), R))  # lanes affected by this block
        hit |= (active & cap)                     # capacity lanes that became nonzero
    return blocks

N = 20000
results = [trial() for _ in range(N)]
print("Average blocks until all capacity lanes nonzero:", statistics.mean(results))


output:
Average blocks until all capacity lanes nonzero: 3.3214

=== Code Execution Successful ===
