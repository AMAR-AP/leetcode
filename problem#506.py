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
            else:class Solution(object):
    def findRelativeRanks(self, score):
        vsort = sorted(score, reverse=True)
        
        rank_map = {}
        for i in range(len(score)):
            if i > 2:
                rank_map[vsort[i]] = str(i + 1)
            elif i == 0:
                rank_map[vsort[i]] = "Gold Medal"
            elif i == 1:
                rank_map[vsort[i]] = "Silver Medal"
            elif i == 2:
                rank_map[vsort[i]] = "Bronze Medal"
        
        ranks = [rank_map[score[i]] for i in range(len(score))]
        
        return ranks
                i+=1
                if i==j:
                    j+=1
                else:
                    result -= 1

        if j==len(nums) and counter+1==result and result>1:
            return counter+1
        return counter