def maxChainLen(Parr, n):
    arr_a =[]
    arr_b =[]
    for pair in Parr:
        arr_a.append(pair.a)
        arr_b.append(pair.b)
    arr_a.sort()
    arr_b.sort()
    max_count = 0

