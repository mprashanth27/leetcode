'''
Sol - https://walkccc.me/LeetCode/problems/912/#__tabbed_3_3
average-case time complexity of O(n log n) &  overall space complexity of O(log n) on average
'''
from typing import List
from random import randint
class Solution:
  def sortArray(self, nums: List[int]) -> List[int]:
    def quickSort(A: List[int], l: int, r: int) -> None:
      if l >= r: # Base case
        return

      def partition(A: List[int], l: int, r: int) -> int:
        randIndex = randint(0, r - l) + l
        A[randIndex], A[r] = A[r], A[randIndex]
        pivot = A[r]
        nextSwapped = l
        for i in range(l, r):
          if A[i] <= pivot:
            A[nextSwapped], A[i] = A[i], A[nextSwapped]
            nextSwapped += 1
        A[nextSwapped], A[r] = A[r], A[nextSwapped]
        return nextSwapped

      m = partition(A, l, r)
      quickSort(A, l, m - 1)
      quickSort(A, m + 1, r)

    quickSort(nums, 0, len(nums) - 1)
    return nums
    
obj = Solution()
print(obj.sortArray([5,2,3,1]))