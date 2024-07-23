class Solution(object):
    def reverseString(self, s):
        n = len(s) - 1
        v = []

        for i in range(n, -1, -1):
            v.append(s[i])
        for i in range(n + 1):
            s[i] = v[i]