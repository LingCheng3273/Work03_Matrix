from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix(4, 0)
matrix2 = new_matrix(4, 4)

print "This is a new empty matrix:"
print_matrix(matrix)

add_edge(matrix, 100, 100, 1, 100, 300, 1)
add_edge(matrix, 100, 300, 1, 300, 300, 1)
add_edge(matrix, 300, 300, 1, 300, 100, 1)
add_edge(matrix, 300, 100, 1, 100, 100, 1)

add_edge(matrix, 200, 200, 1, 100, 100, 1)
add_edge(matrix, 200, 400, 1, 100, 300, 1)
add_edge(matrix, 400, 400, 1, 300, 300, 1)
add_edge(matrix, 400, 200, 1, 300, 100, 1)

add_edge(matrix, 200, 200, 1, 200, 400, 1)
add_edge(matrix, 200, 400, 1, 400, 400, 1)
add_edge(matrix, 400, 400, 1, 400, 200, 1)
add_edge(matrix, 400, 200, 1, 200, 200, 1)
print "added 4 edges:"
print_matrix(matrix)

#draw_lines(matrix, screen, color)

scalar_mult(matrix, 0.25)
print "scaled matrix by half"
print_matrix(matrix)

#draw_lines(matrix, screen, color)

print "this is the identity matrix:"
print_matrix(ident(matrix))

print "identity matrix * matrix:"
matrix_mult(ident(matrix), matrix)
print_matrix(matrix)

matrix_test1= [[1, 1, 1, 1],[1, 1, 1, 1],[1, 1, 1, 1],[1, 1, 1, 1]]
matrix4= matrix[:]
matrix_mult(matrix_test1, matrix4)

draw_lines(matrix, screen, color)
print_matrix(matrix)




print "empty 4x4 matrix * matrix:"
matrix_mult(matrix2, matrix)
print_matrix(matrix)

display(screen)
