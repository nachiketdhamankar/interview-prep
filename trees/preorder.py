"""

"""
from typing import Optional, List


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def preorder_recursive(root: Optional[Node]):
    def preorder_helper(root: Optional[Node], ans: List[int]):
        if root:
            ans.append(root.val)
            preorder_helper(root.left, ans)
            preorder_helper(root.right, ans)

    output = []
    preorder_helper(root, output)
    return output


def preorder_iterative(root: Optional[Node]):
    stack = [root]
    ans = []
    while stack:
        cur = stack.pop()
        if not cur:
            continue
        ans.append(cur.val)
        stack.append(cur.right)
        stack.append(cur.left)
    return ans

root = Node(4)
root.left = Node(9)
root.right = Node(0)
root.left.left = Node(5)
root.left.right = Node(1)

print(f'Preorder Recursive: {preorder_recursive(root)}')
print(f'Preorder Iterative: {preorder_iterative(root)}')
