import math


def print_matrix( matrix ):
    pr=""
    for row in range(len(matrix[0])):
        for col in range(len(matrix)):
            pr=pr+ str(matrix[col][row]) + ", "
        pr=pr+ "\n"
    print pr

def ident( matrix ):
    pass

def scalar_mult( matrix, s ):
    pass

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    pass




def new_matrix(rows = 4, cols = 2):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
