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
    
resForest=[{"name":"Wood", "rarity":1,"timeToBreak":1,"stock":100}]
resMountain=[
    {"name":"Cobble", "rarity":1,"timeToBreak":3,"stock":500},
    {"name":"Coal", "rarity":2,"timeToBreak":5,"stock":100},
    {"name":"Iron", "rarity":5,"timeToBreak":10,"stock":50},
    {"name":"Gold", "rarity":10,"timeToBreak":20,"stock":30},
    {"name":"Diamond", "rarity":20,"timeToBreak":30,"stock":20},
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