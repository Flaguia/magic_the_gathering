import sys, random
sys.path.insert(0, "./Modules/Interface") # Permet de dire que les modules à l'interrieur sont des libraties externes

from Modules import places, Job, Tool, Interface, classe_Joueur, spell

class Personnage:
    def __init__(self, nom, classe="",arme=spell.poing, ability=[]):
        self.nom = nom 
        self.classe = classe
        self.arme = arme
        self.vie = 100
        self.attaque = 15
        self.magie = 40
        self.mana = 400
        self.vitesse = 30
        self.ability = ability

        namePlace, objPlace = random.choice(list(places.items())) # Récupère un lieu random
        self._place = (namePlace, objPlace) # Sauvegarde ce lieu sous forme de dictoinaire
        self._inventaire={"iRessouces":{}, "iWeapons":[], "iArmors":[],"iSpells":[], "iTools":{"Punch":Tool("Punch", 1),"Axes":[Tool("Pioche en bois", 2,5),Tool("Pioche en pierre", 5,5),], "Pickaxes":[], "Swords":[], "Fishing Rods":[]}}
        self.jobs={"Lumberjack":Job("Lumberjack"),
                "Mineur":Job("Mineur"),
                "Hunter":Job("Hunter"),
                "Fisherman":Job("Fisherman")
        }


    def class_choice(self):
        liste_classe = []
        for key in classe_Joueur.classe_choice:
             liste_classe.append(key)

        resKey = Interface.questionary.select( # Pose une question
            "Quel classe choisissez vous ?",
            choices=list(map(str,liste_classe )) # Convertis mes objects en chaine de charactère
        ).ask()
        self.classe = resKey


    def __str__(self):
        capacité = []
        for comp in self.ability:
            capacité.append(comp.name)
        return f'{self.nom}, classe: {self.classe}, vie: {self.vie}, attaque: {self.attaque}, dégat magique: {self.magie}, mana: {self.mana}, vitesse: {self.vitesse}, liste des compétences: {capacité}'


    def work(self):
        #TODO Fix le bug de l'xp de l'outil
        job=self.jobs[self._place[1].job]

        tools=self._inventaire["iTools"][self._place[1].tool] # Récupère la liste des outils possibles
        if len(tools)>0:
            # Demande quel outil choisir
            choicesTools=[str(self._inventaire["iTools"]["Punch"])] # On laisse toujours la possibilité d'utiliser le poing
            for tool in tools: # Pour chaque outils
                if tool.durability[0]<1:
                    choicesTools.append(Interface.Choice(str(tool), disabled="Votre outil est cassé"))
                else:
                    choicesTools.append(str(tool))

            resTool = Interface.questionary.select( # Pose une question
                "Quel outil voulez-vous utiliser ?",
                choices=choicesTools # Convertis mes objects en chaine de charactère
            ).ask()
            print(resTool)
        else: tool=self._inventaire["iTools"]["Punch"]

        ressources=job.work(tool, self._place[1]) # Récupère les ressources.

        # Rajout des ressources dans l'inventaire
        for key in ressources.keys():
            try: self._inventaire["iRessouces"][key]+=ressources[key] # On esssaye d'ajouter le nombre d'elements recupéré dans la ressource deja existante
            except: self._inventaire["iRessouces"][key]=ressources[key] # On creer la ressource dans l'inventaire avec son nombre d'element
                 

    def moove(self):
        choicesPlaces=self._place[1].moovePossibles # Récup les mouvements possibles a partir de ce lieu
        resKey = Interface.questionary.select( # Pose une question
            "Ou voulez-vous aller ?",
            choices=list(map(str, choicesPlaces)) # Convertis mes objects en chaine de charactère
        ).ask()

        self._place=(resKey,places[resKey]) # Sauvegarde la nouvelle place ("nom", obj)
        Interface.print_formatted_text(Interface.HTML(f'Vous vennez de bouger vers : <b>{resKey}</b>'))


    def showInventaire(self):
        invRessources=""
        if self._inventaire["iRessouces"]:
            for key, value in self._inventaire["iRessouces"].items():
                invRessources+=f"<i>{key}</i>: <orange>{value}</orange>\n"
        else: invRessources="<red>Vous n'avez aucunes ressources pour le moment !</red>\n"

        invTools=""
        for key, value in self._inventaire["iTools"].items():
            if key=="Punch":
                invTools+=f"<orange>{value}</orange>\n"
            else:
                temp=""
                for t in value:
                    temp+=f"{str(t)}, "
                invTools+=f"<i>{key}</i>: <orange>{str(temp)[:-2]}</orange>\n"

        Interface.print_formatted_text(Interface.HTML(f'<b><blue>------ Inventaire ------</blue>\n<green>--- Ressources ---</green></b>\n{invRessources}\n<b><green>--- Outils ---</green></b>\n{invTools}'))

    def craft(self):
        typeOfCraft = Interface.questionary.select( # Affiche les choix
            "Que voulez vous craft ?",
            choices=["Outils"]
        ).ask()
        if typeOfCraft=="Outils":
            whatTool = Interface.questionary.select( # Affiche les choix
                "Quel type d'outil voulez vous creer/réparer ?",
                choices=["Axes", "Pickaxes", "Swords", "Fishing Rods"]
            ).ask()

