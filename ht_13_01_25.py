def can_complete_circuit(gas, cost):
    total_gas = total_cost = tank = start_index = 0
    
    for i in range(len(gas)):
        total_gas += gas[i]
        total_cost += cost[i]
        tank += gas[i] - cost[i]
        
        # If tank is negative, cannot start from the current start_index
        if tank < 0:
            start_index = i + 1
            tank = 0
    
    # Check if the total gas is at least equal to the total cost
    return start_index if total_gas >= total_cost else -1

# Example usage
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
print(can_complete_circuit(gas, cost))  # Output: 3

gas = [2, 3, 4]
cost = [3, 4, 3]
print(can_complete_circuit(gas, cost))  # Output: -1


def candy(ratings):
    n = len(ratings)
    candies = [1] * n

    # Traverse left to right
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Traverse right to left
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)

# Example usage
ratings = [1, 0, 2]
print(candy(ratings))  # Output: 5

ratings = [1, 2, 2]
print(candy(ratings))  # Output: 4
