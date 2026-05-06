parcels = [(100,10),(60,20),(120,30)]
capacity = 50

parcels.sort(key=lambda x: x[0]/x[1], reverse=True)

total_value = 0

for v,w in parcels:
    if capacity >= w:
        total_value += v
        capacity -= w

print("Total Value:", total_value)
