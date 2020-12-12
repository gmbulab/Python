"""
@author : Guy-Marcel MBULA (gmbula@yahoo.fr)
@Date : Dec 2020
"""

###################################################################
# Ce chapitre traite des strings et stings formatting en Python   #
###################################################################

# 1.création des strings
# 2.Print des string
# 3.Indexation (slicing) des strings
# 4.Propriétés des strings
# 5.Méthodes des strings
# 6.Print et formatting des strings 

### 1. Création des strings 

# créer un mot 
mot =  "Bonjour"

# une phrase 
phrase = "Bonjour tout le Monde"

# on peut utiliser les simple quotes ou les doubles quotes 
p1 =  'phrase simple quote'
p2 = " phrase double quote"
p3 = " L'est : ceci est une phrase avec un simple et un double quote"

### 2. print de string
print("je print un string en python")
print(p1)
print(phrase , ", comment ça va ? ") # séparé par une virgule
print(phrase + ", comment ça va ? ") # séparé par un +
print(p1, p2) # séparé par une virgule
print(p1 + p2) # séparé par un +

### 3. Indexation (slicing des strings)
#renvoie les éléments en commençant par 0 
# Soit [place de l'élément] soit [debut:fin:step]
# si on ne préceise pas debut on commence par le premier élément, si on ne précise pas fin on va jusqu'au dernier
# Si on ne précise pas step il est de 1 (on récupère tout les éléments)
#  un lien intéressant sur les slicing en python https://zestedesavoir.com/tutoriels/582/les-slices-en-python/
print(p1[0]) # premier élément
print(p1[-1]) # dernier élément

print(p1[1:9:2]) # de 1 à 9 avec un step de 2
print(p1[::]) # Tous les éléments

### 4. Propriétés des trings 
# Les strings sont immutables

### 5. Méthodes des trings
# Les object pythons ont des methodes natives qui sont des fonctions 
# Les méthodes sont appélés avec des points 
print(p1.upper())
print(p1.lower())
print(p1.lower())

### 6. Print et formatting des strings
# https://docs.python.org/3/library/stdtypes.html#old-string-formatting
#  
# On peut utiliser .format() pour ajouter des objects strings avec format à définir
# Il suffit de mettre {} dans la chaine string
p4 = 'Bonjour, nous utilisons {} pour remplir votre nom qui est {}'.format('braket', 'Guy-Marcel')
print(p4)
# on peut également preciser l'ordre 
print(' Le {3} , le {1} et le {2}'.format('second ', 'troisieme' , 'premier' ))

# on peut spécifier la valeur et évite la duplication
print('Le a vaut {a} , le b vaut {b} et le c vaut {c}. {b} est le nombre le plus grand puis vient {c}'.format(a=1, b=25.6 , c =3.14))

# On peut également utiliser % avec le format souhaité
print('Utilisation de %s pour une phrase' %'Pourcentage')
# Avec pourcentage, nous pouvons préciser le format de conversion
# %s  pour string pour  str()
# %r pour string avec les quote 
# %f  pour float soit 
# %d pour integer
print('Votre nom est %s et votre prenom %r' %('MBULA BAKU', 'Guy-Marcel'))
print('Ceci %s sera transformé en string lors du print' %3.75)
print('Le nombre %d est en int et non en float' %3.75)

# Le format peut être plus précis notament pour les floats 
# %m.nf : m  est le nombre max que le nombre peut contenir (remplacer par des blancs si pas atteint)
# n est le ombre de chiffre après la virguel 
print('Nombre float : %6.3f' %156.36965)

# Il est également possible d'avoir plusieurs formats dans une même phrase
print('un string : %s, un integer : %d, un float : %f , un autre string avec quote : %r' %('Bonjour', 3.14658 , 3.145655 , 'pi'))



