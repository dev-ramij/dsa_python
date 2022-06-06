# Root will be whoose parent is itself
# So recursive we are going upward
# when we get new parent update it
def find(sets, a):
    if sets[a] != a:
        sets[a] = find(sets, sets[a])
    return sets[a]


# which ranks are greater it will be opposites parent
# if equal make parent_b's parent as parent_a and increase the rank of parent_a
def union(sets, ranks, a, b):
    parent_a = find(sets, a)
    parent_b = find(sets, b)
    if parent_a == parent_b:
        return
    if ranks[parent_a] > ranks[parent_b]:
        sets[parent_b] = parent_a
    elif ranks[parent_b] > ranks[parent_a]:
        sets[parent_a] = parent_b
    else:
        sets[parent_b] = parent_a
        ranks[parent_a] += 1
