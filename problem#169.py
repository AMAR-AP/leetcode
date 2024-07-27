class Solution:
    def majorityElement(self, nums):
        n=len(nums)
        count=0
        for i in range(n):
            if count==0:
                cur=nums[i]
                count=1
            elif nums[i]==cur:
                count+=1
            else:
                count-=1

        count1=0        
        for i in range(n):
            if nums[i]==cur:
                count1+=1

        if count1>(n/2):
            return cur
        else:
            return -1