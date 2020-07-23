# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # recursive implementation: every time I call the function, it looks at the children of the tree
        # therefore, memorize level by counting the number of times the function is called

        results = [[]]
        level = 0
        
        # If tree is None return empty
        if root is None: 
            return []
            

        # Create two stacks to store nodes in the current 
        # and next level 
        currentLevel = [] 
        nextLevel = [] 
        

        # if ltr is true push nodes from  
        # left to right otherwise from 
        # right to left 
        ltr = True

        # initialize current level with the root of the tree
        currentLevel.append(root)
        
        # while the current level is not empty 
        while len(currentLevel) > 0: 
            # get the whole current level
            temp = currentLevel.pop(-1) 
            
            # append the current level to the results list
            results[level].append(temp.val)
            
            if ltr: 
                # if ltr then next level with go from left to right, so push left first
                if temp.left: 
                    nextLevel.append(temp.left) 
                if temp.right: 
                    nextLevel.append(temp.right) 
            else: 
                # else push right first
                if temp.right: 
                    nextLevel.append(temp.right) 
                if temp.left: 
                    nextLevel.append(temp.left) 

            if len(currentLevel) == 0: 
                # reverse ltr to push node in 
                # opposite order after each level is complete
                ltr = not ltr 
                # swap of stacks 
                currentLevel, nextLevel = nextLevel, currentLevel
                
                results.append([])
                level += 1
                
        return results[:-1]