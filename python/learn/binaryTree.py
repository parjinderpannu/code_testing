#           1
#       2       3
#     4   5    10
# Binary Search Trees (BSTs)
    #         5
    #     1       8
    #   -1  3   7   9
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

# Check if Value Exists (DFS) Time: O(n), Space: O(n)
    def search(self, target):
        # Base case: Check if the current node's value matches the target
        if self.val == target:
            return True

        # Check left child only if it exists
        left_result = self.left.search(target) if self.left else False

        # Check right child only if it exists
        right_result = self.right.search(target) if self.right else False

        # Return True if either the left or right subtree contains the target
        return left_result or right_result
    

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

    A2 = TreeNode(5)
    B2 = TreeNode(1)
    C2 = TreeNode(8)
    D2 = TreeNode(-1)
    E2 = TreeNode(3)
    F2 = TreeNode(7)
    G2 = TreeNode(9)

    A2.left, A2.right = B2, C2
    B2.left, B2.right = D2, E2
    C2.left, C2.right = F2, G2

    print("Root node:", A)
    print()
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
    print(f"Search(7): {A.search(7)}")
    print(f"Search(10): {A.search(10)}")
    print(f"A2.in_order(): {A2.in_order()}")



if __name__ == "__main__":
    main()