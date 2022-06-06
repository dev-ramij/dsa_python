def multisetPower(N,A):
    maxValue = max(A)
    power = 0
    popIdx = []
    for i in range(N):
        if A[i] == maxValue+1 or A[i] == maxValue -1:
            popIdx.append(i)
    for i in range(len(popIdx)):
        A.pop(popIdx[i])
    for i in range(len(A)):
        power += A[i]
    return power


print(multisetPower(2,[1,3]))