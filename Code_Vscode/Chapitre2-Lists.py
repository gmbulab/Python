"""
@author : Guy-Marcel MBULA BAKU (gmbula@yahoo.fr)
@Date : Jan 2021
"""

###################################################################
# Ce chapitre traite des listes e de leur utilisation  en Python  #
###################################################################
# 1. Création des listes , L'indexation et le slicing
# 2. Les méthodes sur les listes 
# 3. Les nested listes 


# 1. Création des listes,  l'indexation et le slicing
#####################################################
# Création
# - Les listes sont mutables et sont crées avec des []
# - Elles peuvent contenir différents types 

ma_liste = [1.36,2,3,'a','b','c']

# L'indeation
# Pour indexer une liste, on utilise [n], avec n la place de l'élément de la liste en partant de 0 par ordre croissant ou de -1 par ordre décroissant 

premier_elmt = ma_liste[0] # Renvoie 1.36
second_elmt = ma_liste[1] # Renvoie 2
dernier_elmt = ma_liste[-1] # renvoie c

# Le slicing 
# Le slicing permet de récupérer plusieurs élements d'une liste. La syntaxe est le suivant : ma_liste [debut:fin:pas*]. 
# Le pas est facultatif (un pas de 1 est considére si on ne précise pas), l'élément début est inclu et fin est exclu, si on ne précise pas début ou fin, il considère le premier et dernier élément

slicing1 = ma_liste[0:4:2] # renvoie les éléments 0 inclu à 4 exclu avec un pas de 2 soit 1.36, 3
slicing2 = ma_liste[0:4] # renvoie les éléments 0 inclu à 4 exclu  soit 1.36,2 et 3
slicing3 = ma_liste[:4] # équivant à slicing 2, renvoit les élément du début à 4


# 2. Les méthodes sur les listes 
#################################
###### Les listes ont des méthodes prédéfines, nous présenterons quelques unes ici
## Ajout d'un élément à la fin : liste.append(elmt_à_ajouter)

ma_liste.append('ajout par append') # Attention, votre liste est modifiée de manière permanente
# Pour éviter une modification permanante, on copie la liste 
ma_liste1 = ma_liste
ma_liste1.append('second append')

## suppression d'un élément avec pop : liste.pop(n), avec n la place de l'élement à supprimer
ma_liste1.pop(0) # comme append, l'opération est permanente 

## supression d'un élément avec remove : liste.remove(elmy_à supprimer)
ma_liste1.remove('a')

## concatenation de liste : liste+liste1
ma_liste2 = ['l','m',5,3.3,6]
concatliste = ma_liste + ma_liste2 # renvoie une nouvelle liste conteant [1.36, 2, 3, 'a', 'b', 'c', 'ajout par append', 'l', 'm', 5, 3.3, 6]

## inversion de liste avec reverse : liste.reverse()
concatliste.reverse()

# trie de liste (trie par ordre alhabetique ou croissant) : liste.sort 
ma_liste2 = [5,3.3,6]
ma_liste2
.sort()

# 3. Les Nested listes ou liste de liste
#########################################

nest_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
nested_list = [ma_liste, ma_liste1, ma_liste2]

# L'indixation se fait de la même manière 
nest_list[0] # renvoie [1, 2, 3]
nest_list[0][0] # renvoie 1

print(ma_liste2.index(5))






