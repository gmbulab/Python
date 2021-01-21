"""
@author : Guy-Marcel MBULA BAKU (gmbula@yahoo.fr)
@Date : Jan 2021
"""

###################################################
# Ce chapitre traite des boucles whiles en python #
###################################################
# 1. Création des boucles whiles 
# 2. Break, continue, pass

# La syntaxe d'une boucle while est la suivante : 
"""
while test :
    fait quelque chose 
else : 
    fait ça
"""
#Exemple simple
x = 0
while x < 5:
    print('x is currently: ',x)
    print(' x est plus petit que 5, ajouter 1 to x')
    x+=1

x = 0

while x < 10:
    print('x is currently: ',x)
    print(' x est plus petit que 5, ajouter 1 to x')
    x+=1
    
else:
    print('x plus grand que 5, je sors de la boucle!')

# On peut ajouter les options suivantes : 
# break : arrête au niveau du loop
# continue : va au prochain niveau du loop
# pass : passe et ne fais rien

# Exemple de break et continue : 
while x < 5 : 
    print('x vaut', x 'donc inferieur à 5')
    x+=1
    if x==3: 
        print('x==3')
        print('Break à x = 3')
        break
    else : 
        continue 
