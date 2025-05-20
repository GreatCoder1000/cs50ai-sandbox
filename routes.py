import dfs

# Each node is a key-value pair where the key is the node name and the value is
# a list of key-value pairs that are the place that it connects to and the 
# distance there.

diagram = {
    "bergen": [
        {"voss": (104.0, [])}
    ],
    "voss": [
        {"bergen": (104.0, [])},
        {"vinje": (19.0, [])},
        {"kjerland": (24.7, [])}
    ],
    "vinje": [
        {"voss": (19.0, [])},
        {"hønefoss": (332.0, [])}
    ],
    "kjerland": [
        {"voss": (24.7, [])},
        {"hardangerbrua": (10.8, [])}
    ],
    "hardangerbrua": [
        {"kjerland": (10.8, [])},
        {"hønefoss": (266.0, [])}
    ],
    "hønefoss": [
        {"vinje": (332.0, [])},
        {"hardangerbrua": (266.0, [])},
        {"oslo": (59.5, [])}
    ],
    "oslo": [
        {"hønefoss": (59.5, [])}
    ]
}

print(dfs.find_shortest_route_from_to(diagram, "oslo", "bergen"))