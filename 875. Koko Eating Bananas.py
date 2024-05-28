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
                    time -= (piles[i] // k)
                    i += 1
                if (time <= 0):
                    break
            if (i == len(piles) - 1 and time >= 0):
                return k

obj = Solution()
print(obj.minEatingSpeed([3,6,7,11],8))