#           1
#       2       3
#     4   5    10
from collections import deque
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

    # Recursive Pre-order Traversal (DFS) Time: O(n), Space: O(n)
    def pre_order(self):
        if not self:
            return
        print(self)  # Print the current node's value
        if self.left:  # Recursively traverse the left subtree
            self.left.pre_order()
        if self.right:  # Recursively traverse the right subtree
            self.right.pre_order()
    
    # Recursive In-order Traversal (DFS) Time: O(n), Space: O(n)
    def in_order(self):
        if not self:
            return
        if self.left:  # Recursively traverse the left subtree
            self.left.in_order()
        print(self)  # Print the current node's value
        if self.right:  # Recursively traverse the right subtree
            self.right.in_order()
    
    # Recursive In-order Traversal (DFS) Time: O(n), Space: O(n)
    def post_order(self):
        if not self:
            return
        if self.left:  # Recursively traverse the left subtree
            self.left.post_order()
        if self.right:  # Recursively traverse the right subtree
            self.right.post_order()
        print(self)  # Print the current node's value
    
    def pre_order_iterative(self):
        stk = [self]
        while stk:
            self = stk.pop()
            print(self)
            if self.right: stk.append(self.right)
            if self.left: stk.append(self.left)
    
# Level Order Traversal (BFS) Time: O(n), Space: O(n)
    def level_order(self):
        q = deque()
        q.append(self)

        while q:
            self = q.popleft()
            print(self)
            if self.left: q.append(self.left)
            if self.right: q.append(self.right)

def main():
    # Creating the binary tree
    A = TreeNode(1)
    B = TreeNode(2)
    C = TreeNode(3)
    D = TreeNode(4)
    E = TreeNode(5)
    F = TreeNode(10)

    A.left = B
    A.right = C
    B.left = D
    B.right = E
    C.left = F

    print("Root node:", A)
    print("Pre-order Traversal:")
    A.pre_order() 
    print("In-order Traversal:")
    A.in_order()  
    print("Post-order Traversal:")
    A.post_order()  
    print("Pre-order-iterative Traversal:")
    A.pre_order_iterative() 
    print("Level-order Traversal:")
    A.level_order()  

if __name__ == "__main__":
    main()