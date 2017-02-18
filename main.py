from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

print("Here is your original matrix:")
print_matrix(matrix)
add_edge(matrix, 0, 0, 0, 500, 500, 500)
#draw_lines(matrix, screen, color)
print("Here is your new matrix")
print_matrix(matrix)

print("This the the multiplicative identity of your matrix")
print_matrix(ident(matrix))

print("Here is your matrix after *2")
scalar_mult(matrix, 2)
print_matrix(matrix)




#display(screen)
