# La place est commune à touts les personages


class Place:
    def __init__(self, name, ressources, job, tool):
        self.name=name
        self.ressources=ressources
        self.job=job
        self.tool=tool
        self.mobs=[]

    def spawnMob(self):
        return

resForest=[{"name":"Wood", "multiplier":1},{"name":"Cobble", "multiplier":0.1}]
resMine=[
    {"name":"Cobble", "multiplier":1},
    {"name":"Coal", "multiplier":0.7},
    {"name":"Iron", "multiplier":0.4},
    {"name":"Gold", "multiplier":0.2},
    {"name":"Diamond", "multiplier":0.05},
    ]

forest=Place("Forest",  resForest, "Lumberjack", "Axe")
mine=Place("Mine",  resMine, "Mineur", "Pickaxe")
plaine=Place("Plaine", [], "Hunter", "Sword")
