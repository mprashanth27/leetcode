class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # Recursive approach: T = O(logn), M = O(logn)
        def binarySearch(l,h):
            if (l > h): # Base case
                return -1
            mid = l + (h - l) // 2 # this approach is safer especially in langs. other than py.
            # mid = (l + h) // 2 # didn't work earlier bcoz I didn't return BS calls at lines - 12, 14, 16

            if(nums[mid] == target):
                return mid
            elif (nums[mid] > target): # target lies on the left of mid 
                return binarySearch(l,mid - 1)
            else: # target lies on the right of mid 
                return binarySearch(mid + 1, h)
            
        return binarySearch(0, len(nums) - 1)

obj = Solution()
print(obj.search([-1,0,2,4,6,8], 6))