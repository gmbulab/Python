#########################################
## penser à faire les list comprehension

# Let's make three lists
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

# Make a list of lists to form a matrix
matrix = [lst_1,lst_2,lst_3]
# Build a list comprehension by deconstructing a for loop within a []
first_col = [row[0] for row in matrix]

#####################################################
# Self addition and self substractions
x = 1 
x +=2 # équivaut ) x = x +2 >> renvoie 3

######################################################
# Enumerate 
l = 'abcde'
for i, x  in enumerate(l) : 
    print("A l'index {} , nous avons {}".format(i,x)) # i ; numéro de l'index de 0 à la fin et x tous les éléments de l
# On peut créer une liste avec le deux : 
liste = list(enumerate(l)) # [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd'), (4, 'e')]

######################################################
# Zip
liste1 = [1,2,3,4,5]
liste2 = ['a','b','c','d','e']

zip(liste1, liste2) #[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]

name = 'This is a global name'

