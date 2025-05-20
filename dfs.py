# DEPTH FIRST SEARCH

def find_all_routes_diagram_from_to(neural, start, end):
    routes = []

    def dfs(node, target, path, children):
        if node == target:
            routes.append(path + [node])
            return
        for child_dict in children:
            for child, grandchildren in child_dict.items():
                dfs(child, target, path + [node], grandchildren)

    dfs(start, end, [], neural[start])
    return routes

def find_all_routes_with_cost(neural, start, end):
    routes = []

    def dfs(node, target, path, cost):
        if node == target:
            routes.append((path + [node], cost))
            return
        for child_dict in neural.get(node, []):
            for child, (edge_cost, _) in child_dict.items():
                if child not in path:  # Prevent cycles
                    dfs(child, target, path + [node], cost + edge_cost)

    dfs(start, end, [], 0)
    return routes

def find_shortest_route_from_to(neural, start, end):
    all_routes = find_all_routes_with_cost(neural, start, end)
    if not all_routes:
        return None
    shortest_route = min(all_routes, key=lambda x: x[1])
    return shortest_route

# Example usage:
if __name__ == "__main__":
    diagram = {
                "A": [
                    {"B": (2, [  # 2 is the distance from A to B
                        {"C": (4, [  # 4 is the distance from B to C
                            {"E": (7, [])}  # 7 is the distance from C to E
                        ])},
                        {"D": (1, [  # 1 is the distance from B to D
                            {"F": (100, [])}  # 100 is the distance from D to F
                        ])}
                    ])},
                    {"G": (5, [
                        {"H": (2, [
                            {"I": (1, [
                                {"F": (2, [])}
                            ])}
                        ])}
                    ])}
                ]
            }

    shortest_route = find_shortest_route_from_to(diagram, "A", "F")
    print(shortest_route)  # Output: (['A', 'B', 'D', 'F'], 6)