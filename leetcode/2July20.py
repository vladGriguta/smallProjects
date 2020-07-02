# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        # recursive implementation: every time I call the function, it looks at the children of the tree
        # therefore, memorize level by counting the number of times the function is called
        if root:
            output = [[root.val]]
            def f(root,level):

                if(root.left):
                    if len(output)<=level:
                        output.insert(0,[])
                    loc = len(output)-level-1
                    output[loc].append(root.left.val)
                    f(root.left,level+1)
    
                if(root.right):
                    if len(output)<=level:
                        output.insert(0,[])
                    loc = len(output)-level-1
                    output[loc].append(root.right.val)
                    f(root.right,level+1)
            
            f(root,1)
            
            return output
        else:
            return []

            
        