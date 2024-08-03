class Solution(object):
    def findLHS(self, nums):
        nums = sorted(nums)
        if len(nums)==1: return 0
        if len(nums)==2:
            if nums[1]-nums[0]==1:
                return 2
            else:
                return 1

        i,j = 0,1
        counter = 0
        result = 1
        while j<len(nums):
            if nums[j]-nums[i]==0 or nums[j]-nums[i]==1:
                if nums[j]-nums[i]==1:
                    counter = max(counter, result+1)
                j+=1
                result += 1
                if j==len(nums):
                    break
            else:
                i+=1
                if i==j:
                    j+=1
                else:
                    result -= 1

        if j==len(nums) and counter+1==result and result>1:
            return counter+1
        return counter