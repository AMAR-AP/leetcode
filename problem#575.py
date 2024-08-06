class Solution:
    def distributeCandies(self, candyType):
        return min(len(list(set(candyType))),int(len(candyType)/2))