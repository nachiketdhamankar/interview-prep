"""

"""

from typing import Optional


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bfs_iterative(root: Optional[Node]):
    queue = [root]
    output = []
    while queue:
        cur = queue.pop(0)
        if cur:
            output.append(cur.val)
            queue.append(cur.left)
            queue.append(cur.right)
    return output


root = Node(4)
root.left = Node(9)
root.right = Node(0)
root.left.left = Node(5)
root.left.right = Node(1)

print(bfs_iterative(root))
