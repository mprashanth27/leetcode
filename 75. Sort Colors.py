class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # NC's 1 pass approach
        l = 0 # 0 writer ptr
        r = len(nums) - 1 # 2 writer ptr
        i = 0 # reader ptr
        while (i <= r):
            if (nums[i] == 0):
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif (nums[i] == 2):
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
                i -= 1
            else:
                i += 1

obj = Solution()
nums = [2,0,2,1,1,0]
obj.sortColors(nums)
print(nums)