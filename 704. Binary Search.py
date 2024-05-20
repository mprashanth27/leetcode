class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def binarySearch(l,h):
            if (l > h): # Base case?
                return -1
            mid = (l + h) // 2

            if(nums[mid] == target):
                return mid
            elif (nums[mid] > target): # target lies on the left of mid 
                binarySearch(l,mid - 1)
            else: # target lies on the right of mid 
                binarySearch(mid + 1, h)
            
        binarySearch(0, len(nums) - 1)

obj = Solution()
print(obj.search([-1,0,2,4,6,8], 4))