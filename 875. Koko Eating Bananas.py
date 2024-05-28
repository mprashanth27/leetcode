class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Brute force
        for k in range(1,max(piles)+1):
            i, time = 0, 0
            while (i <= len(piles) - 1):
                if (piles[i] <= k):
                    i += 1
                    time += 1
                else:
                    piles[i] -= k
                    time += 1
                if (time > h):
                    break
            if (i == len(piles) - 1 and time <= h):
                return k

obj = Solution()
print(obj.sortArray([3,6,7,11],8))