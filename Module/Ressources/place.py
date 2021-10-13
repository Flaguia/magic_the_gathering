
class Place:
    def __init__(self, name, ressources):
        self.name=name
        self.ressources=ressources


resForest=[{"ressource":"Wood", "multiplier":1},{"ressource":"Cobble", "multiplier":0.1}]
resMine=[
    {"ressource":"Cobble", "multiplier":1},
    {"ressource":"Coal", "multiplier":0.7},
    {"ressource":"Iron", "multiplier":0.4},
    {"ressource":"Gold", "multiplier":0.2},
    {"ressource":"Diamond", "multiplier":0.05},
    ]

forest=Place("Forest",  resForest)
mine=Place("Mine",  resMine)