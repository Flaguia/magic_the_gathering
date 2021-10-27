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
        self._inventaire={"iRessouces":{}, "iWeapons":[], "iArmors":[],"iSpells":[], "iTools":{"Punch":Tool("Punch", 1),"Axes":[Tool("Hache en bois", 2, [(30,"Bois")],200),Tool("Hache en pierre", 5,[(20,"Bois"), (10,"Pierre")],500)], "Pickaxes":[], "Swords":[], "Fishing Rods":[]}}
        self.jobs={"Lumberjack":Job("Lumberjack"),
                "Mineur":Job("Mineur"),
                "Hunter":Job("Hunter"),
                "Fisherman":Job("Fisherman")
        }


    def __str__(self):
        capacité = []
        for comp in self.ability:
            capacité.append(comp.name)
        return f'{self.nom}, classe: {self.classe}, vie: {self.vie}, attaque: {self.attaque}, dégat magique: {self.magie}, mana: {self.mana}, vitesse: {self.vitesse}, liste des compétences: {capacité}'


    def class_choice(self):
        liste_classe = []
        for key in classe_Joueur.classe_choice:
             liste_classe.append(key)

        resKey = Interface.questionary.select( # Pose une question
            "Quel classe choisissez vous ?",
            choices=list(map(str,liste_classe )) # Convertis mes objects en chaine de charactère
        ).ask()
        self.classe = resKey


    def work(self):
        #TODO Fix le bug de l'xp de l'outil
        job=self.jobs[self._place[1].job]

        tools=self._inventaire["iTools"][self._place[1].tool] # Récupère la liste des outils possibles
        if len(tools)>0:
            # Demande quel outil choisir
            choicesTools=[str(self._inventaire["iTools"]["Punch"])] # On laisse toujours la possibilité d'utiliser le poing
            for tool in tools: # Pour chaque outils
                if tool.durability[0]<1:
                    choicesTools.append(Interface.questionary.Choice(str(tool), disabled="Votre outil est cassé"))
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
                    if t.durability[0]<1:
                        temp+=f"<red><i>{str(t)}</i></red>, "
                    else:
                        temp+=f"<orange>{str(t)}</orange>, "
                invTools+=f"<i>{key}</i>: {str(temp)[:-2]}\n"

        Interface.print_formatted_text(Interface.HTML(f'<b><blue>------ Inventaire ------</blue>\n<green>--- Ressources ---</green></b>\n{invRessources}\n<b><green>--- Outils ---</green></b>\n{invTools}'))

    def _bolRessources(self, liste): # [(20,"Bois"),(20,"Fer")]
        for element in liste:
            try: # On essaye de voir si le nombre de stock est superieur
                if self._inventaire["iRessouces"][element[1]]<element[0]:
                    return False
            except: # On a même pas trouvé la ressource dans les stocks
                return False
        return True


    def craft(self):
        typeOfCraft = Interface.questionary.select( # Affiche les choix
            "Que voulez vous craft ?",
            choices=["Outils"]
        ).ask()
        if typeOfCraft=="Outils":
            whatTool = Interface.questionary.select( # Affiche les choix
                "Quel type d'outil voulez vous creer/réparer ?",
                choices=["Hache", "Pioche", "Epee", "Canne à pêche"]
            ).ask()
            if whatTool=="Hache":
                listOfTools=["Hache en Bois (30 bois)", "Hache en pierre (20 bois, 10 pierre)","Hache en fer (20 bois, 10 fer)", "Hache en or (20 bois, 10 fer)", "Hache en Diamants (20 bois, 10 fer)"]
                choix=["Ne rien faire"]
                for tool in self._inventaire["iTools"]["Axes"]:
                    if tool.durability[0]!=tool.durability[1]: # Test si outil usé
                        requirement=str(tool.requirement[-1][0]//2)+" "+tool.requirement[-1][1]
                        stringName=f"Réparer {tool.name} ({requirement})"                        
                        if not self._bolRessources([(tool.requirement[-1][0]//2,tool.requirement[-1][1])]): # Test si assez de ressources
                            choix.append(Interface.questionary.Choice(stringName, disabled="Vous n'avez pas assez de ressources"))
                        else:
                            choix.append(stringName)

                typeOfTool = Interface.questionary.select( # Affiche les choix
                "Quel Hache veut-tu réparer/crafter ?",
                    choices=choix
                ).ask()

