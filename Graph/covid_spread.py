class Solution:

    def infect(self, row, col, hospital):
        hospital[row][col] = 2

    def getInfectedPatient(self, row_l, col_l, hospital):
        ceils = []
        for row in range(row_l):
            for col in range(col_l):
                if hospital[row][col]==2:
                    ceils.append([row, col])
        return ceils

    def hasHealthy(self, hospital, row_l, col_l):
        for row in range(row_l):
            for col in range(col_l):
                if hospital[row][col] == 1:
                    return True
        return False

    # Check if there is any healthy person or not
    # get all infected patients
    # infect neighbors of that person
    # check if anyone infect in that time
    # if not infected and has healthy person then all can't be ifected
    # return count
    def helpaterp(self, hospital):
        count = 0
        row_l = len(hospital)
        col_l = len(hospital[0])
        hasHealthy = self.hasHealthy(hospital, row_l, col_l)
        while hasHealthy:
            count+=1
            infected = False
            infectedCeils = self.getInfectedPatient(row_l, col_l, hospital)
            for ceil in infectedCeils:
                row = ceil[0]
                col = ceil[1]
                if row + 1 < row_l and hospital[row + 1][col] == 1:
                    infected = True
                    self.infect(row + 1, col, hospital)
                if row - 1 >= 0 and hospital[row - 1][col] == 1:
                    infected = True
                    self.infect(row - 1, col, hospital)
                if col + 1 < col_l and hospital[row][col + 1] == 1:
                    infected = True
                    self.infect(row, col + 1, hospital)
                if col - 1 >= 0 and hospital[row][col - 1] == 1:
                    infected = True
                    self.infect(row, col - 1, hospital)
            hasHealthy = self.hasHealthy(hospital, row_l, col_l)
            if hasHealthy and not infected:
                return -1
        return count