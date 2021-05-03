"""
@author : Guy-Marcel MBULA BAKU (gmbula@yahoo.fr)
@Date : Dec 2020
"""

####################################################
# Ce chapitre traite des tuples et set  en Python   #
#####################################################
##### Les tuples
# 1.création des tuples
# 2.Quelques méthodes sur les tuples 
# 3.Immutabilité des tuples
# 4.Quand utiliser les tuples 

# Création d'un tuple 
t = (1,2,3)

# Quelques méthodes surle slicing 
len(t) # taille 
t[0]  # slicing

# Contrairement aux listes , les tuples sont immutables 
t[0] = 'change' # ne marche pas 
t.append('nope') # Ne marche pas 


####### Les sets 
