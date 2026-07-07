'''
Problem : Gas Station

Pattern : Greedy

Key Idea :

Maintain a candidate starting station.

If the fuel (tank) becomes negative,
it means we cannot reach the next station.

Hence, every station between the current
starting station and this failed station
is also impossible.

So, directly move the starting station
to the next index.

Finally, if the total amount of gas
is less than the total cost,
completing the circle is impossible.

Time Complexity : O(n)

Space Complexity : O(1)
'''

gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

# Candidate starting station
start = 0

# Fuel available while travelling
tank = 0

# Overall fuel balance of the whole journey
total = 0

for i in range(len(gas)):

    # Fuel gained/lost at current station
    diff = gas[i] - cost[i]

    # Update current fuel
    tank += diff

    # Update overall fuel balance
    total += diff

    # Cannot reach the next station
    if tank < 0:

        # Skip all previous stations
        start = i + 1

        # Start fresh from the next station
        tank = 0

# If total fuel is enough, answer exists
if total >= 0:
    print(start)
else:
    print(-1)