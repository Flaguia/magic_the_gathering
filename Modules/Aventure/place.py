# La place est commune à touts les personages

class Place:
    def __init__(self, name, ressources, job, tool):
        self.name=name
        self.ressources=ressources
        self.job=job
        self.tool=tool
        self.mobs=[]
        self.moovePossibles=[]

    def __str__(self):
        return self.name

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
plain=Place("Plain", [], "Hunter", "Sword")
river=Place("River", [], "Fisherman", "Fishing Rod")
swamp=Place("Swamp", [], "Fisherman", "Fishing Rod")
desert=Place("Desert", [], "Hunter", "Sword")


forest.moovePossibles=[mountain,river,plain,desert]
mountain.moovePossibles=[forest,river]
plain.moovePossibles=[river,forest,desert]
river.moovePossibles=[plain,swamp,mountain,forest]
swamp.moovePossibles=[river]
desert.moovePossibles=[plain,forest]

places={"Forest":forest, "Mountain":mountain, "Plain":plain, "River":river, "Swamp":swamp, "Desert":desert}