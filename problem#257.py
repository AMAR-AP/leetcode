class Solution(object):
    def binaryTreePaths(self, root):
        res=[]
        def dfs(root,ans=""):
            if not root:return
            if not root.left and not root.right:
                res.append(ans+str(root.val))
            dfs(root.left,ans+str(root.val)+'->')
            dfs(root.right,ans+str(root.val)+'->')
        dfs(root,"")
        return res