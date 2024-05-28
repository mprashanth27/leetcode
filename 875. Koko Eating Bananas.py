from math import ceil
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # Brute force
        for k in range(1,max(piles)+1):
            i, time = 0, h
            while (i <= len(piles) - 1):
                if (piles[i] <= k):
                    i += 1
                    time -= 1
                else:
                    time -= ceil(piles[i] / k)
                    i += 1
                if (time <= 0):
                    break
            if (i == len(piles) and time >= 0): # not using len(piles)-1 to balance the inc that happens at line 12 before exiting while loop
                return k

obj = Solution()
print(obj.minEatingSpeed([3,6,7,11],8))