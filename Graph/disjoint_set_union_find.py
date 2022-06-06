# function should return parent of x
# Root will be whoose parent is itself
# So recursive we are going upward
def find(A, X):
    if A[X] == X:
        return X
    return find(A,A[X])

# Find parent_x and parent_z
# assign parents of parent_z to parent_x
def unionSet(A, X, Z):
    
    parent_x = find(A,X)
    parent_z = find(A,Z)
    if parent_x == parent_z:
        return
    A[parent_z] = parent_x