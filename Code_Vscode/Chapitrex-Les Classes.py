"""
@author : Guy-Marcel MBULA BAKU (gmbula@yahoo.fr)
@Date : Jan 2021
inspiré du cours de pieran Data et de python crash course
"""

###################################################################
# Ce chapitre traite de la programmation orientée Object en Python
# et des classes  #
###################################################################
# 1. Création d'une classe 
# 2. Les attibuts et les méthodes d'une classe
# 3. 

# En python tout est considéré comme un objet : 
# Pour créer des users define object on utilise class. A partir d'une classe on peut créer 
# des instances qui sont des objects spécifiques d'une classe
# Un Attribut est une caractéristique d'un object et une méthode est une opération qu'on peut réaliser sur un object

# La fonction inti d'une classe 
# _init_ : toujours crée après l'object, elle va contenir l'initialisation des différents attributs de la classe

#  Il est égelement possible de définir un 'class object attributes' qui sera générale dans la classe. 
# Par exemple pour Dog, on définit "mamal"
# Exemple d'une classe
class Dog : 
    # La classe Object attribut 
    species = "mammal"
    def __init__(self, breed, name) : 
        self.breed = breed
        self.name = name
sam = Dog('lab', 'sam')
print(sam.breed)
print(sam.name)