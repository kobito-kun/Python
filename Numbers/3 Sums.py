incomplete
class Solution(object):
	def threeSum(self, nums):
		results = []
		for b in range(len(nums)):
			for c in range(len(nums)):
				if nums[0] + nums[b] + nums[c] == 0:
					print("yes")

print(Solution().threeSum([-1,0,1,2,-1,-4]))