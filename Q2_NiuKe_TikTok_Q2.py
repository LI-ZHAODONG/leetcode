# ChatGPT and it passed ... ...
import sys


def count_ambush_schemes(N, D, positions):
    MOD = 99997867

    count = 0
    j = 0

    for i in range(N):
        while j < N and positions[j] - positions[i] <= D:
            j += 1
        # j-1 is the largest index where positions[j-1] - positions[i] <= D
        k = j - 1
        if k - i >= 2:
            count += (k - i) * (k - i - 1) // 2
            count %= MOD

    return count


# Read input
data = sys.stdin.read().split()
N = int(data[0])
D = int(data[1])
positions = list(map(int, data[2:]))

# Compute and print the result
print(count_ambush_schemes(N, D, positions))
