class Solution:

    #Function to find starting point where the truck can start to get through
    #the complete circle without exhausting its petrol in between.
    def tour(self, lis, n):
        petrol = 0
        dis = 0
        # check if circular tour is possible or not
        for i in range(n):
            petrol += lis[i][0]
            dis += lis[i][1]

        if dis > petrol:
            return -1
        left_petrol = 0
        start_idx = 0
        # find index
        for i in range(n):
            left_petrol += (lis[i][0] - lis[i][1])
            # if no petrol is left
            if left_petrol < 0:
                start_idx = i + 1
                left_petrol = 0
        return start_idx
