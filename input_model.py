# Graph (distance matrix)
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Parcels (value, weight, time window)
parcels = [
    {"value": 100, "weight": 10},
    {"value": 60, "weight": 20},
    {"value": 120, "weight": 30}
]

vehicle_capacity = 50

print("Graph:", graph)
print("Parcels:", parcels)
