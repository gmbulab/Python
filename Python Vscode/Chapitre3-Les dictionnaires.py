"""
@author : Guy-Marcel MBULA BAKU (gmbula@yahoo.fr)
@Date : Janv 2021
"""

###########################################
# Ce chapitre traite des dictionnaires    #
###########################################

# 1. Création des dictionnaires
# 2. Accès aux objects d'un dictionnaires
# 3. Les Nested dictionnaires
# 4. Méthodes des dictionnaires

# Les dictionnaires sont considérés comme des mappings (hash tables dans d'autres langages)
# Les "mappings" sont des collection d'objects qui sont stockés avec une clé et une valeur associée. 

#######################################################
# 1.  la création des dictionnaires
# Les dictionnaires sont construits avec des {}
# Ils peuvent être créés vides 
dict_vide = {}
# Les clés et valeurs y sont ajoutées de la manière suivante
dict_vide['c1'] = 'val1'
dict_vide['c2'] = 'val2'

# Ils peuvent égalent être créés avec les clés et valeurs de la manière suivante
mon_dict = {"cle1":"valeur1" , "cle2":"valeur2"}

# les dictionnaires acceptent preque tous les types comme valeur et peuvent être de types différents
mon_dict1 = {'cle1':123,'cle2':[1,2,3],'cle3':['l0','l1','l2']}

###############################################
#  2. L'accès aux objects d'un dictionnaire
# on accède aux object en indéxant la clé associée. 
# La valeur renvoyée est du type de la valeur, avec les propriétés et méthodes associées. 
mon_dict1["cle2"] # Renvoie valeur2 (de type Sting)
mon_dict1["cle3"] # Renvoie ['l0','l1','l2'] (de type liste)
mon_dict1["cle3"][0] # Renvoie 'l0'


###############################################
# 3. Les nested dictionnaires
# Dictionnaire dans un dictionnaire dans un autre dictionnaore
dict_nest = {'cle1':{'cle1_1':{'cle1_1_1':'val'}}}
dict_nest['cle1']['cle1_1']['cle1_1_1'] # Renvoie val


#################################################
# 4. Quelques methodes sur les dictionnaires
# Liste des clés 
mon_dict.keys()

# Liste des valeurs
mon_dict1.values

# Tuple clé, valeur
mon_dict1.items()

# Suppresion avec pop
# dict.pop(cle, default*) : si clé existe alors supprime clé sinon default. 
#                         : Si clé n'exite pas et default non spécifie, alors erreur
mon_dict1.pop


