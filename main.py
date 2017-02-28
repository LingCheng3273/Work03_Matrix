from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix(4, 0)

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
print "added 12 edges"
print_matrix(matrix)

draw_lines(matrix, screen, color)

scalar_mult(matrix, 0.25)
print "scaled matrix by 1/4"
print_matrix(matrix)

draw_lines(matrix, screen, color)

print "this is the identity matrix:"
print_matrix(ident(matrix))

print "identity matrix * matrix:"
identity= ident(matrix)
matrix_mult(identity, matrix)
print_matrix(matrix)

print "identity matrix * 3:"
scalar_mult(identity, 3)
print_matrix(identity)

print "(new identity matrix) * matrix:"
matrix_mult(identity, matrix)
print_matrix(matrix)

draw_lines(matrix, screen, color)

display(screen)
