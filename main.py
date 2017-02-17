from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()


print_matrix(matrix)
add_edge(matrix, 0, 0, 0, 500, 500, 500)
draw_lines(matrix, screen, color)
print_matrix(matrix)

display(screen)
