class Solution(object):
  def twoSum(self, nums, target):
    for a in range(len(nums)):
      for i in range(len(nums)):
        print(a, i)
        if a == i:
          pass
        else:
          if nums[a] + nums[i] == target:
            return [a, i]

print(Solution().twoSum([3,3], 6))