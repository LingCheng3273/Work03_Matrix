import math


def print_matrix( matrix ):
    pr=""
    for row in range(len(matrix[0])):
        for col in range(len(matrix)):
            pr=pr+ str(matrix[col][row]) + ", "
        pr=pr+ "\n"
    print pr

def ident( matrix ):
    m=[]
    for c in range( len(matrix) ):
        m.append( [] )
        for r in range(len(matrix)):
            m[c].append(0)
    for c in range( len(m) ):
        m[c][c]=1
    return m

def scalar_mult( matrix, s ):
    for c in range(len(matrix)):
        for r in range(len(matrix[0])):
            matrix[c][r]= matrix[c][r] * s

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    r1= len(m1[0])
    c1= len(m1)
    r2= len(m2[0])
    c2= len(m2)
    for r in range(r1):
        for c in range(c2):
            m2[r][c]= m1[0][r]*m2[c][0] + m1[1][r]*m2[c][1] + m1[2][r]*m2[c][2] + m1[3][r]* m2[r][3]
        



def new_matrix(rows = 4, cols = 2):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
