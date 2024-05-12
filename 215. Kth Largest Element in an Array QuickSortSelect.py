from random import randint
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        #adaptation of Nc's Sol [Quick Select Algo.] by modifying my quicksort code 
        k = len(nums) - k
        def quickSelect(nums,L,R):
            if (L >= R): #Base Case
                return
            
            def partition(A, l, r):
                randIndex = randint(0, r - l) + l
                A[randIndex], A[r] = A[r], A[randIndex] #moving the rand element to the end for comparsion
                pivot = A[r]
                nextSwapped = l # Writer ptr ~ element to swap with 
                for i in range(l, r):
                    if (A[i] <= pivot): #if element <= curr pivot
                        A[nextSwapped], A[i] = A[i], A[nextSwapped]
                        nextSwapped += 1
                A[nextSwapped], A[r] = A[r], A[nextSwapped] # put curr pivot at its right position
                return nextSwapped 


            M = partition(nums, L, R) # Pivot
            if (M == k): # if kth value = partition value
                return nums[k]
            elif (k < M): # if kth value lies on the left of partition value i.e., smaller 
                quickSelect(nums, L, M-1) # Sort Left of current Pivot
            elif (k > M): # if kth value lies on the right of partition value i.e., greater
                quickSelect(nums, M+1, R) # Sort right of current Pivot

        quickSelect(nums, 0, len(nums)-1)
        return nums[k]
    
obj = Solution()
print(obj.findKthLargest([5,2,3,1],2))