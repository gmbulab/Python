## penser à faire les list comprehension

# Let's make three lists
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

# Make a list of lists to form a matrix
matrix = [lst_1,lst_2,lst_3]
# Build a list comprehension by deconstructing a for loop within a []
first_col = [row[0] for row in matrix]