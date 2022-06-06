class Solution:
    
    # traverse the row through the column if find 0 
    # then there is atleast one member who don't know him 
    def knownToAll(self,col,M,n):
        
        for row in range(n):
            if row != col and M[row][col] == 0:
                return False
        return True
        
    # if all columns of the corresponding row is 0 then he knows none 
    def knowsNone(self,row,M,n):
        for col in range(n):
            if M[row][col] == 1:
                return False
        return True
        
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # traverse column wise if we found 0 then there may be possibility of celebrity
        for i in range(n):
            if M[i][0] == 0 and self.knownToAll(i,M,n) and self.knowsNone(i,M,n):
                return i
        return -1
