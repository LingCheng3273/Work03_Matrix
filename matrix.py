import math


def print_matrix( matrix ):
    pr="[["
    if (len(matrix) >0):
        for row in range(len(matrix[0])):
            for col in range(len(matrix)):
                pr= pr + str(matrix[col][row]) + ", "
            pr = pr[0: len(pr)-2] + "]\n["
        print pr[0: len(pr)-2]+"]"
    else:
        print "[]"

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
            matrix[c][r]= int(matrix[c][r] * s)

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    for r in range(4):
        for c in range(len(m2)):
            m2[c][r]= int(m1[0][r]*m2[c][0] + m1[1][r]*m2[c][1] + m1[2][r]*m2[c][2] + m1[3][r]* m2[r][3])

def new_matrix(rows, cols):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

