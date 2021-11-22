"""

"""
from typing import Optional, List


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def postorder_recursive(root: Optional[Node]):
    def postorder_helper(root: Optional[Node], ans: List[int]):
        if root:
            postorder_helper(root.left, ans)
            postorder_helper(root.right, ans)
            ans.append(root.val)

    output = []
    postorder_helper(root, output)
    return output


def postorder_iterative(root: Optional[Node]):
    pass


root = Node(4)
root.left = Node(9)
root.right = Node(0)
root.left.left = Node(5)
root.left.right = Node(1)
root.right.left = Node(8)
print(f'postorder Recursive: {postorder_recursive(root)}')
print(f'postorder Iterative: {postorder_iterative(root)}')
