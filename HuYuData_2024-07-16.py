# # We use a
# DP
# table
# to
# store
# the
# maximum
# value
# that
# can
# be
# obtained
# with different capacities of the knapsack.
#
# python
# Copy
# code


def knapsack_0_1(weights, values, capacity):
    n = len(weights)

    # Initialize a 2D list to store maximum values
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Build the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    # Maximum value is stored in dp[n][capacity]
    return dp[n][capacity]


# Example usage:
weights = [1, 2, 3, 4, 5]
values = [10, 20, 30, 40, 50]
capacity = 7
print(f"The maximum value that can be put in the knapsack is: {knapsack_0_1(weights, values, capacity)}")