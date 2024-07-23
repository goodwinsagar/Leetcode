from typing import List

class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    k=0
    for i in range(1, len(nums)):
      if nums[i] != nums[k]:
          k += 1
          nums[k] = nums[i]
    nums = nums[:k+1]
    return k + 1

nums = [0,0,1,1,1,2,2,3,3,4]
Solution().removeDuplicates(nums)
