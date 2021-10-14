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
resMountain=[
    {"name":"Cobble", "multiplier":1},
    {"name":"Coal", "multiplier":0.7},
    {"name":"Iron", "multiplier":0.4},
    {"name":"Gold", "multiplier":0.2},
    {"name":"Diamond", "multiplier":0.05},
    ]

forest=Place("Forest",  resForest, "Lumberjack", "Axe")
mountain=Place("Mountain",  resMountain, "Mineur", "Pickaxe")
plaine=Place("Plaine", [], "Hunter", "Sword")
river=Place("River", [], "Fisherman", "FishingRod")
swamp=Place("River", [], "Fisherman", "FishingRod")

places={"Forest":forest, "Mountain":mountain, "Plaine":plaine, "River":river, "Swamp":swamp}