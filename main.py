from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix(4, 2)
matrix2= new_matrix(4,1)
matrix3= new_matrix(4,4)

##print("Here is your original matrix:")
##print_matrix(matrix)
##add_edge(matrix, 0, 0, 0, 500, 500, 500)
###draw_lines(matrix, screen, color)
##print("Here is your new matrix")
##print_matrix(matrix)
##
##print("This the the multiplicative identity of your matrix")
##print_matrix(ident(matrix))
##
##print("Here is your matrix after *2")
##scalar_mult(matrix, 2)
##print_matrix(matrix)

print("This is a new matrix")
print_matrix(matrix2)

print("Here is your matrix after adding edges")
add_edge(matrix2, 0, 0, 0, 5, 5, 5)
print_matrix(matrix2)

print("Here is your matrix after *2")
scalar_mult(matrix2, 2)
print_matrix(matrix2)

print("Here is your matrix after matrix mult")
matrix_mult(matrix3, matrix2)
print_matrix(matrix2)

#display(screen)
