class Person:
    def __init__(self, nom):
        self.nom = nom

    def dire_bonjour(self):
        print(f"Bonjour, je m'appelle {self.nom}")

# Création d'une instance de la classe Person
personne = Person("Alice")

# Utilisation de la réflexivité pour accéder à la méthode dire_bonjour
methode = getattr(personne, "dire_bonjour")

# Appel de la méthode à l'exécution
methode()

# Utilisation de la réflexivité pour modifier l'attribut nom
setattr(personne, "nom", "Bob")

# Affichage de la modification
print(f"Nouveau nom : {personne.nom}")
