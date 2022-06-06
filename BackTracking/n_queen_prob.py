class Solution:

    def trackQueens(self, track, n, results, prevIdx, count):
        if len(track) == n:
            results.append(list(track))
            return
        remaining_track = []
        for i in range(1, n + 1):
            if i not in track and (prevIdx < n + 1 and i != prevIdx + 1) and (
                    prevIdx > 1 and i != prevIdx - 1):
                remaining_track.append(i)
            elif i not in track and prevIdx == 1 and i != prevIdx + 1:
                remaining_track.append(i)
            elif i not in track and prevIdx == n + 1 and i != prevIdx - 1:
                remaining_track.append(i)
        if len(remaining_track) == 0:
            return
        all_track = []
        for i in remaining_track:
            temp_track = track[:]
            temp_track.append(i)
            all_track.append(temp_track)
        for tr in all_track:
            self.trackQueens(tr, n, results, tr[len(tr) - 1], count + 1)

    def nQueen(self, n):
        result = []
        for i in range(1, n + 1):
            self.trackQueens([i], n, result, i, 1)
        return result


ob = Solution()
print(ob.nQueen(9))
