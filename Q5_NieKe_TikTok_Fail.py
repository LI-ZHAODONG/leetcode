# def tsp(cost):
#     n = len(cost)
#     # memoization table to store the minimum cost of visiting each subset of cities ending at each city
#     dp = [[float('inf')] * n for _ in range(1 << n)]
#     dp[1][0] = 0  # starting point
#     return dp
#
#
#
# n = int(input().strip())
# cost = []
# for _ in range(n):
#     cost.append(list(map(int, input().strip().split())))
#
# # Calculate and print the minimum cost
# print(tsp(cost))


def tsp(cost):
    n = len(cost)
    # memoization table to store the minimum cost of visiting each subset of cities ending at each city
    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1][0] = 0  # starting point

    # Iterate over all subsets of cities
    for mask in range(1 << n):
        for u in range(n):
            if mask & (1 << u):  # if u is in the subset represented by mask
                for v in range(n):
                    if not mask & (1 << v):  # if v is not in the subset represented by mask
                        dp[mask | (1 << v)][v] = min(dp[mask | (1 << v)][v], dp[mask][u] + cost[u][v])

    # Return the minimum cost of visiting all cities and returning to the starting point
    min_cost = float('inf')
    for u in range(1, n):
        min_cost = min(min_cost, dp[(1 << n) - 1][u] + cost[u][0])

    return min_cost


# Read input
n = int(input().strip())
cost = []
for _ in range(n):
    cost.append(list(map(int, input().strip().split())))

# Calculate and print the minimum cost
min_cost = tsp(cost)
print(min_cost)