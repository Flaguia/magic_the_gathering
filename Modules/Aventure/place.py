# Les palces sont les mêmes pour touts les joueurs
from .repetedFunction import RepeatedTimer
from random import randint

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
    
    def reStock(self):
        i=randint(0,len(self.ressources)-1) # On tente d'ajouter une ressource random
        if self.ressources[i]["stock"]<self.ressources[i]["stockMax"]: 
            self.ressources[i]["stock"]+=1
        else: #On en rajoute une obligatoirement
            for i in range(len(self.ressources)): # On boucle alors sur toutes les ressources
                if self.ressources[i]["stock"]<self.ressources[i]["stockMax"]: 
                    self.ressources[i]["stock"]+=1
                    break #On stop la boucle

# Les listes des ressources 
resForest=[
    {"name":"Bois", "rarity":1,"timeToBreak":1,"stock":50,"stockMax":50},
    {"name": "Champignon", "rarity":5,"timeToBreak":5, "stock":10,"stockMax":10},
    {"name": "Fruit douteux", "rarity":10,"timeToBreak":10, "stock":2,"stockMax":2},
]

resMountain=[
    {"name":"Pierre", "rarity":1,"timeToBreak":3,"stock":50,"stockMax":50},
    {"name":"Charbon", "rarity":2,"timeToBreak":5,"stock":10,"stockMax":10},
    {"name":"Fer", "rarity":5,"timeToBreak":10,"stock":50,"stockMax":50},
    {"name":"Or", "rarity":10,"timeToBreak":20,"stock":30,"stockMax":30},
    {"name":"Diamand", "rarity":20,"timeToBreak":30,"stock":10,"stockMax":10},
]

resPlain = [
    {"name": "Viande", "rarity":2,"timeToBreak":10, "stock":50,"stockMax":50},
    {"name": "Viande de poulet", "rarity":2,"timeToBreak":20, "stock":50,"stockMax":50},
    {"name": "Viande de vélociraptor", "rarity":2,"timeToBreak":10, "stock":50,"stockMax":50},
    {"name": "Pomme", "rarity":5,"timeToBreak":3, "stock":10,"stockMax":10},
    {"name": "Légume", "rarity":10,"timeToBreak":50, "stock":10,"stockMax":10},
]

resRiver = [
    {"name": "Poisson", "rarity":1,"timeToBreak":20, "stock":50,"stockMax":50},
    {"name": "Algue", "rarity":2,"timeToBreak":10, "stock":10,"stockMax":10},
    {"name": "Calamar", "rarity":5,"timeToBreak":5, "stock":2,"stockMax":2},
]

resSwamp =  [
    {"name": "Os", "rarity":2,"timeToBreak":2, "stock":50,"stockMax":50},
    {"name": "Champignon vénéneux", "rarity":2,"timeToBreak":5, "stock":10,"stockMax":10},
    {"name": "Grimoire déchiré", "rarity":5,"timeToBreak":15, "stock":5,"stockMax":5},
    {"name": "Débris de métal", "rarity":5,"timeToBreak":15, "stock":5,"stockMax":5},
]

resDesert = [
    {"name": "Cactus", "rarity":1,"timeToBreak":10, "stock":50,"stockMax":50},
    {"name": "Poison de scorpion", "rarity":10,"timeToBreak":5, "stock":2,"stockMax":2},
]


# On génère nos places
forest=Place("Forest",  resForest, "Lumberjack", "Axes")
mountain=Place("Mountain",  resMountain, "Mineur", "Pickaxes")
plain=Place("Plain", resPlain, "Hunter", "Swords")
river=Place("River", resRiver, "Fisherman", "Fishing Rods")
swamp=Place("Swamp", resSwamp, "Fisherman", "Fishing Rods")
desert=Place("Desert", resDesert, "Hunter", "Swords")

# On créé les liaisons entre les places
forest.moovePossibles=[mountain,river,plain,desert]
mountain.moovePossibles=[forest,river]
plain.moovePossibles=[river,forest,desert]
river.moovePossibles=[plain,swamp,mountain,forest]
swamp.moovePossibles=[river]
desert.moovePossibles=[plain,forest]

# On exporte un dictionnaire avec comme clef les noms et comme valeur les object correspondant
places={"Forest":forest, "Mountain":mountain, "Plain":plain, "River":river, "Swamp":swamp, "Desert":desert}

def addRessourcesInAllPlaces():
    #TODO en restok 1 aléatoirement

    forest.reStock()
    mountain.reStock()
    plain.reStock()
    river.reStock()
    swamp.reStock()
    desert.reStock()

repeat = RepeatedTimer(1, addRessourcesInAllPlaces) # Repete la fonction toutes les 5 secondes
