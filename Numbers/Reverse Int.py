class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
        	res = int("-" + str(abs(x))[::-1])
        	if res < -2**31 or res > 2**31:
        		return 0
        	else:
        		return res
        else:
        	res = int(str(x)[::-1])
        	if res < -2**31 or res > 2**31:
        		return 0
        	else:
        		return res        	
        

print(Solution().reverse(1999999))