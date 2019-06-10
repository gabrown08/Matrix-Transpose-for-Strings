print('MATRIX TRANSPOSE FOR STRINGS by Greg Brown')
print()

m = input('A is an m by n matrix. m =  ')
while type(m) != type(1):
    try:
        m = int(m)
    except ValueError:
        print()
        print('error: the input was not an integer. enter an integer.')
        m = input('m =  ')
print()

n = input('A is an m by n matrix. n =  ')
while type(n) != type(1):
    try:
        n = int(n)
    except ValueError:
        print()
        print('error: the input was not an integer. enter an integer.')
        n = input('n =  ')
print()

A = []

for i in range(m):
    print('enter each entry for row ' + str(i + 1) + ':')
    row = []
    for j in range(n):
        entry = input()
        row.append(entry)
    A.append(row)
    print()
    
print('matrix A: ')
for i in range(m):
    print(A[i])

print()

B = [[0 for i in range(m)] for j in range(n)]

print('A transpose: ')
for i in range(n):
    for j in range(m):
        B[i][j] = A[j][i]
    print(B[i])

print()
input('press enter to exit.')
