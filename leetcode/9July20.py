# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to insert nodes in level order
def insertLevelOrder( arr, root, i, n): 
    # Base case for recursion
    if i < n:
        temp = TreeNode(val=arr[i])
        root = temp
  
        # insert left child only if not None
        if ((2*i+1 < n) and arr[2*i+1]):
            root.left = insertLevelOrder(arr, root.left,
                                         2 * i + 1, n)
  
        # insert right child only if not None
        if ((2*i+2 < n) and arr[2*i+2]):
            root.right = insertLevelOrder(arr, root.right, 
                                          2 * i + 2, n)

    return root


class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # looking at the edge cases, it seems like it is impossible to compute the solution
        # to this problem without going through all nodes in the tree.
        # Therefore, we will try a brute force approach:
        # 1. Go through each and every node.
        # 2. For each node, memorize the number of times you went left and right from the parrent nodes
        # 3. For each level compute the maximum distance between two nodes
        
        # base case 
        if not root: return 0
        a = [(root, 1)]
        res = 0
        while a:
            width = a[-1][1] - a[0][1] + 1
            res = max(res, width)
            new_a = []
            for tup in a:
                node, count = tup[0], tup[1]
                if node.left:
                    new_a.append((node.left, 2*count))
                if node.right:
                    new_a.append((node.right, 2*count + 1))
            a = new_a
                    
        return res


        """

        if root:
            output = []
            # each call of the function needs the root node, current level and the difference between
            # the number of times the current path went right and left.
            # by convention, right is +1 and left is -1

            def f(root,level,path):
                print('\n')
                # if the output vector does not have the dimension for the current level, append one
                print('level=',level)
                print('root.val',root.val)

                if(root.left):
                    if len(output) <= level:
                        output.append([0] * (2**(level+1)))

                    path_local = path.copy()
                    path_local.append(0)

                    loc = sum([path_local[i]*2**i for i in range(len(path_local),1,1)])
                    
                    # add the left_right counter to the vector memorizing the results
                    output[level][loc] = 1

                    print('output=',output)
                    print('path_local=',path_local)
                    print('loc=',loc)
                    
                    # call function recursively on the current node
                    f(root.left,level+1,path_local)

                if (root.right):
                    print(root.val)
                    print(root.right.val)
                    print('double')
                if(root.right):
                    print('double')
                    if len(output) <= level:
                        output.append([0] * (2**(level+1)))

                    path_local = path.copy()
                    path_local.append(1)

                    loc = sum([path_local[i]*2**i for i in range(len(path_local),1,1)])

                    print('right')
                    print('output=',output)
                    print('path_local=',path_local)
                    print('loc=',loc)

                    # add the left_right counter to the vector memorizing the results
                    output[level][loc] = 1
                    
                    # call function recursively on the current node
                    f(root.right, level+1, path_local)
                
            path = []

            f(root,0,path)
            
            print(output)
            # now that we have the array we just need to compute the maximum 
            # distance between nodes on the horizontal axis
            max_width = 0
            for i in range(len(output)):
                line = output[i]

                leftmost_pos = 0
                while (line[leftmost_pos] == 0) and leftmost_pos<len(line)-1:
                    leftmost_pos = leftmost_pos + 1

                rightmost_pos = len(line) - 1
                while (line[rightmost_pos] == 0) and rightmost_pos>=0:
                    rightmost_pos = rightmost_pos - 1

                if(rightmost_pos-leftmost_pos + 1 > max_width):
                    max_width = rightmost_pos-leftmost_pos + 1
                

            return max_width
        else:
            return 0
        

"""
test1 = [1,3,2,5,4,None,9]
test = [1,1,1,1,None,None,1,1,None,None,1]
# build tree
root = insertLevelOrder(test, None, 0, len(test))

#print(root.left.left.val)


sol = Solution()
width = sol.widthOfBinaryTree(root)
print(width)

