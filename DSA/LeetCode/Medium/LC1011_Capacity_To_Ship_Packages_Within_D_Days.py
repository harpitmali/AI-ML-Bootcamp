def ship_within_days(weights, days):
    left = max(weights)
    right = sum(weights)

    while left <= right:
        capacity = (left + right) // 2
        days_needed = 1
        current_weight = 0

        for weight in weights:
            if current_weight + weight > capacity:
                days_needed += 1
                current_weight = 0
            
            current_weight += weight

        if days_needed <= days:
            right = capacity - 1
        else:
            left = capacity + 1

    return left


weights = [1,2,3,4,5,6,7,8,9,10]
days = 5

print(ship_within_days(
    weights,
    days
))