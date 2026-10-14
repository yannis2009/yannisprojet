import json
class Personnage:
   

    def __init__(self, nom, points_de_vie, force):
        self.nom = nom
        self.points_de_vie = points_de_vie
        self.force = force

    def est_vivant(self):
        return self.points_de_vie > 0

    def subir_degats(self, degats):
        self.points_de_vie-= degats
        if self.points_de_vie < 0:
            self.points_de_vie= 0
            
    def to_dict(self):
        return {type(self).__name__: {
            "nom": self.nom,
            "points_de_vie": self.points_de_vie,
            "force": self.force
        }}
    def sauvegarder(self,chemin: str):
        with open(chemin, 'w') as fichier:
            json.dump(self.to_dict(), fichier, indent=4)
    
    def attaquer(self, cible:"Personnage"):
        cible.subir_degats(self.force)
        return (f"{self.nom} attaque {cible.nom} et lui inflige {self.force} degats")
    
    def __repr__(self):
       return (f"{self.nom}({self.points_de_vie} PV)")

class Heros(Personnage):

    def __init__(self,nom,points_de_vie,force,mana:int):
        super().__init__(nom,points_de_vie,force)
        self.mana= mana

    def competence_spéciale(self, cible):
        if self.mana > 10:
            self.mana-= 10
            cible.subir_degats(2*self.force)
            return(f"{self.nom} utilise sa competence speciale sur {cible.nom} et lui inflige {2*self.force} degats")
        else:
            return (f"Votre mana n'est pas suffisant pour effectuer cette competence")


    def to_dict(self):
        return {type(self).__name__: {
            "nom": self.nom,
            "points_de_vie": self.points_de_vie,
            "force": self.force,
            "mana": self.mana
        }}

class Monstre(Personnage):

    def __init__(self,nom,points_de_vie,force ,niveau_de_danger:int,butin:str):
        super().__init__(nom,points_de_vie,force)
        self.niveau_de_danger=niveau_de_danger
        self.butin=butin

    def to_dict(self):
        return {type(self).__name__: {
            "nom": self.nom,
            "points_de_vie": self.points_de_vie,
            "force": self.force,
            "niveau_de_danger": self.niveau_de_danger,
            "butin": self.butin
        }}

    def attaque_monstre(self,cible):
        super().attaquer(cible)
        self.force = self.force * self.niveau_de_danger
        return (f"{self.nom} attaque {cible.nom} et lui inflige {self.force} degats")

class Partie:
    def __init__(self,personnages:list,historique:list):
        self.personnages = []
        self.historique = []

    def ajouter_personnage(self,personnage:Personnage):
        self.personnage.append(personnage)

    def combat(self,attaquant:Personnage,defenseur:Personnage):
        super().attaque()
        if defenseur.est_vivant == False:
            return (f"{defenseur.nom} est vaincu")
        else:                                  

            return self.historique . append (f"{attaquant.nom} attaque {defenseur.nom} et lui fait retire {attaquant.force}")

    def sauvegarder_partie(self,chemin):
        pass

            

        











yannis = Personnage("yannis", 20,7) 
gobelin = Personnage("Gobelin", 20, 5)
aldric = Heros("Aldric", 30, 8, 50)
diablotin=Monstre("diablotin",40,50,2,"20 pieces d'or")
yannis.ajouter_personnage(yannis)
#print(aldric.attaquer(gobelin))
#gobelin.subir_degats(20)
#print(gobelin.points_de_vie)
#print(aldric.__repr__())
#print(aldric.competence_spéciale(gobelin))
#print(diablotin.attaque_monstre(aldric))
#print(aldric.points_de_vie)
#print(gobelin.to_dict())
#print(aldric.sauvegarder("data.json"))

##################
def charger_personnage(chemin:str):
    with open(chemin, 'r') as fichier:
        data = json.load(fichier)
        if "Heros" in data:
            heros_data = data["Heros"]
            return Heros(heros_data["nom"], heros_data["points_de_vie"], heros_data["force"], heros_data["mana"])
        elif "Monstre" in data:
            monstre_data = data["Monstre"]
            return Monstre(monstre_data["nom"], monstre_data["points_de_vie"], monstre_data["force"], monstre_data["niveau_de_danger"], monstre_data["butin"])
        else:
            return ValueError("Type de personnage inconnu dans le fichier JSON.")

lancelot = Heros("Lancelot", 40, 10, 30)

lancelot.sauvegarder("lancelot.json")
lancelot_recharge = charger_personnage("lancelot.json")
print(lancelot_recharge)
print(lancelot_recharge.mana)