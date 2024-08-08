class Solution(object):
    def reverseVowels(self, s):
        vowels = set('aeiouAEIOU')
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            if s[left] not in vowels:
                left += 1
            if s[right] not in vowels:
                right -= 1class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost)<=2:
            return min(cost)
        dp = [cost[0],cost[1]] +[0]*(len(cost)-2)
        for i in range(len(cost)-2):
            dp[i+2] = min(dp[i]+cost[i+2],dp[i+1]+cost[i+2])
        return min(dp[-1],dp[-2])     
                
            
        return ''.join(s)