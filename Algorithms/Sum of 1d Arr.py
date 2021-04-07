nums = [3,1,2,10,1]
v = 0

for i in range(len(nums)):
	nums[i], v = v + nums[i], v + nums[i]

print(nums)