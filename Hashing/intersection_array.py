class Solution:
    def NumberofElementsInIntersection(self,a, b, n, m):
        hashMap = {}
        for i in range(n):
            # store all value of array a into hashMap 
            hashMap[a[i]] = i
        count = 0
        
        for i in range(m):
            # if b[i] present into hashMap and counting as first time
            if b[i] in hashMap and hashMap[b[i]] == 0:
                count+=1
                # preventing count again
                hashMap[b[i]] =1
        return count