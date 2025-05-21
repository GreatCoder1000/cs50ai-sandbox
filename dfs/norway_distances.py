# Each node is a key-value pair where the key is the node name and the value is
# a list of key-value pairs that are the place that it connects to and the 
# distance there.

diagram = {
    "bergen": [
        {"voss": 104.0},
        {"haugesund": 135.0},
    ],
    "voss": [
        {"bergen": 104.0},
        {"vinje": 19.0},
        {"kjerland": 24.7}
    ],
    "vinje": [
        {"voss": 19.0},
        {"hønefoss": 332.0}
    ],
    "kjerland": [
        {"voss": 24.7},
        {"hardangerbrua": 10.8}
    ],
    "hardangerbrua": [
        {"kjerland": 10.8},
        {"hønefoss": 266.0}
    ],
    "hønefoss": [
        {"vinje": 332.0},
        {"hardangerbrua": 266.0},
        {"oslo": 59.0}
    ],
    "oslo": [
        {"hønefoss": 59.0},
        {"drammen": 43.0},
    ],
    "kristiansand": [
        {"haukeli": 235.0},
        {"hirtshals": 371.0},
        {"haugesund": 304.0},
        {"timenes": 8.5}
    ],
    "haugesund": [
        {"kristiansand": 304.0},
        {"bergen": 135.0},
        {"haukeli": 172.0},
    ],
    "drammen": [
        {"arendal": 208.2},
        {"oslo": 43.0},
        {"haukeli": 206.0}
    ],
    "haukeli": [
        {"haugesund": 172.0},
        {"kristiansand": 235.0},
        {"brunkeberg": 76.2}
    ],
    "hirtshals": [
        {"kristiansand": 371.0}
    ],
    "grimstad": [
        {"timenes": 38.3},
        {"arendal": 15.5}
    ],
    "arendal": [
        {"grimstad": 23.0},
        {"drammen": 215.7},
        {"hynnekleiv": 30.0}
    ],
    "timenes": [
        {"kristiansand": 8.5},
        {"grimstad": 38.3},
        {"hynnekleiv": 57.5}
    ],
    "hynnekleiv": [
        {"timenes": 57.5},
        {"arendal": 30.0},
        {"svenes": 2.7},
    ],
    "svenes": [
        {"hynnekleiv": 2.7},
        {"steane": 91.1},
    ],
    "steane": [
        {"svenes": 91.1},
        {"vrådal": 6.2}
    ],
    "vrådal": [
        {"steane": 6.2},
        {"brunkeberg": 17.7}
    ],
    "brunkeberg": [
        {"vrådal": 17.7},
        {"haukeli": 76.2},
        {"drammen": 129.8}
    ],
}