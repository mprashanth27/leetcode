class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # NC's 1 pass logic - Time Complexity: O(n),Space Complexity: O(1)
        l = 0 # 0's writer ptr
        r = len(nums) - 1 # 2's writer ptr
        i = 0 # reader ptr
        while (i <= r):
            if (nums[i] == 0):
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
                i += 1
            elif (nums[i] == 2):
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1 # we are not updating i here inorder to crosscheck if the element we swapped 2 with is 0 or not in the next iteration.
            else: #if (nums[i] == 1), continue to next element
                i += 1

obj = Solution()
nums = [2,0,1]
obj.sortColors(nums)
print(nums)