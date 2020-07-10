
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        # Strategy:
        # 1. Iterate through an infinite loop
        # 2. If find a child to the current node, store the node and go to it's child
        # 3. Else if find the next element, go to that element
        # 4. Else if list of stored nodes connected by child is not null, get the last item in the list
        #    and check if it has a next element. 
        #        If it does, go to that element.
        #        If it does not, delete element from the list and go to 4
        
        # initialize new list
        if head:
            if head.child:
                new_list = Node(head.val,None,head.child,None)
            elif head.next:
                new_list = Node(head.val,None,head.next,None)
            else:
                return head
        else:
            return head
        
        res = []
        node_child_list = []
        
        while True:
            res.append(head.val)
            
            if head.child:
                node_child_list.append(head)
                print('child ',head.val)
                head = head.child
                  
                new_list.next = Node(head.val,None,None,None)
                new_list.next.prev = new_list
                new_list = new_list.next
                
                
            elif head.next:
                print('next ',head.val)
                head = head.next
                
                new_list.next = Node(head.val,None,None,None)
                new_list.next.prev = new_list
                new_list = new_list.next
                
            elif node_child_list:
                print('prev node ',head.val)
                if node_child_list[-1].next:
                    head = node_child_list[-1].next
                    new_list.next = Node(head.val,None,None,None)
                    new_list.next.prev = new_list
                    new_list = new_list.next
                del node_child_list[-1]
                
            else:
                break
                
        print('gets here')
        print(res)
        
        while new_list.prev:
            new_list = new_list.prev
        
        return new_list


test1 = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
