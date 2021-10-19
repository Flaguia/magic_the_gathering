# Les palces sont les mêmes pour touts les joueurs

class Place:
    """
        Un object place qui correspond a un endroit sur la map.
        Il a comme attribut:
        - Un nom
        - Une liste de ressources
        - Un type de métier et d'outil
        - La liste de tous les mobs combattable a cet endroit
        - Les mouvements vers d'autre places possibles (Voir map.txt)     
    """
    
    def __init__(self, name, ressources, job, tool):
        """
            Fonction initialisation:
                name: Un str
                ressources: Une liste de dictionnaire de la forme -> [{"name":str, "rarity":int,"timeToBreak":int,"stock":int},...]
                job: Un str
                tool: Un str          
        """
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

# Les listes des ressources 
resForest=[{"name":"Wood", "rarity":1,"timeToBreak":1,"stock":100}]
resMountain=[
    {"name":"Cobble", "rarity":1,"timeToBreak":3,"stock":500},
    {"name":"Coal", "rarity":2,"timeToBreak":5,"stock":100},
    {"name":"Iron", "rarity":5,"timeToBreak":10,"stock":50},
    {"name":"Gold", "rarity":10,"timeToBreak":20,"stock":30},
    {"name":"Diamond", "rarity":20,"timeToBreak":30,"stock":20},
    ]

# On génère nos places
forest=Place("Forest",  resForest, "Lumberjack", "Axes")
mountain=Place("Mountain",  resMountain, "Mineur", "Pickaxes")
plain=Place("Plain", [], "Hunter", "Swords")
river=Place("River", [], "Fisherman", "Fishing Rods")
swamp=Place("Swamp", [], "Fisherman", "Fishing Rods")
desert=Place("Desert", [], "Hunter", "Swords")

# On créé les liaisons entre les places
forest.moovePossibles=[mountain,river,plain,desert]
mountain.moovePossibles=[forest,river]
plain.moovePossibles=[river,forest,desert]
river.moovePossibles=[plain,swamp,mountain,forest]
swamp.moovePossibles=[river]
desert.moovePossibles=[plain,forest]

# On exporte un dictionnaire avec comme clef les noms et comme valeur les object correspondant
places={"Forest":forest, "Mountain":mountain, "Plain":plain, "River":river, "Swamp":swamp, "Desert":desert}
