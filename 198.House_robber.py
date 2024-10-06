class Solution:
    def rob(self, nums: list[int]) -> int:
        res = 0
        nums_cpy = nums.copy()
        visited = set()
        unvisitable = set() # neighbours of visited homes

        while (nums_cpy):
            max_val = max(nums_cpy)
            max_val_index = nums_cpy.index(max_val)

            if (max_val_index not in visited and max_val_index not in unvisitable):
                res += max_val

                visited.add(max_val_index) 
                nums_cpy.pop(max_val_index)
                
                if (max_val_index != len(nums_cpy) - 1): #check if we popped the last element, as there will be no adj house on right
                    unvisitable.add(max_val_index + 1)
                    nums_cpy.pop(max_val_index) # for popping (max_val_index + 1)'s val as it's index decrements by 1 after popping max_val
                
                if (max_val_index != 0): #check if we popped the first element, as there will be no adj house on left
                    unvisitable.add(max_val_index - 1)
                    nums_cpy.pop(max_val_index - 1)
        
        return res
    
test_obj = Solution()

nums = [1,2,3,1]
test_obj.rob(nums)