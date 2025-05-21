import dfs
from norway_distances import diagram

print("Welcome to the trip planner!")

loc = input("Enter your location:                     > ").strip().lower()
if loc not in diagram.keys():
    while True:
        loc = input("Location not found. Please try again.    > ").strip().lower()
        if loc in diagram.keys():
            break

loc = loc.lower()

dest = input("Enter your destination:                  > ").strip().lower()
if dest not in diagram.keys():
    while True:
        dest = input("Destination not found. Please try again. > ").strip().lower()
        if dest in diagram.keys():
            break

dest = dest.lower()
print(f"Recommended route from {loc.title()} to {dest.title()}:")
shortest_route = dfs.find_shortest_route_from_to(diagram, loc, dest)
via = shortest_route[0][1:-1]
print(f"Distance: {round(shortest_route[1])} km")
if via:
    print(f"Via {', '.join(via)}")

# Show alternative routes
all_routes = dfs.find_all_routes_with_cost(diagram, loc, dest)

# Max reasonable distance for alternatives
max_reasonable = shortest_route[1] * 1.5  # 50% longer than shortest

# Remove the shortest route from alternatives
alternatives = [route for route in all_routes if route != shortest_route and route[1] <= max_reasonable]

if alternatives:
    print("\nAlternative routes:")
    for route, cost in sorted(alternatives, key=lambda x: x[1]):
        via_alt = route[1:-1]
        print(f"Distance: {round(cost)} km", end="")
        if via_alt:
            print(f" via {', '.join(via_alt)}")
        else:
            print()
else:
    print("\nNo reasonable alternative routes found.")