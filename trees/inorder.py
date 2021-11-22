"""

"""
from typing import Optional, List


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inorder_recursive(root: Optional[Node]):
    def inorder_helper(root: Optional[Node], ans: List[int]):
        if root:
            inorder_helper(root.left, ans)
            ans.append(root.val)
            inorder_helper(root.right, ans)

    output = []
    inorder_helper(root, output)
    return output


def inorder_iterative(root: Optional[Node]):
    cur = root
    stack = []
    ans = []
    while cur or stack:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            ans.append(cur.val)
            cur = cur.right
    return ans


root = Node(4)
root.left = Node(9)
root.right = Node(0)
root.left.left = Node(5)
root.left.right = Node(1)
root.right.left = Node(8)
print(f'inorder Recursive: {inorder_recursive(root)}')
print(f'inorder Iterative: {inorder_iterative(root)}')
