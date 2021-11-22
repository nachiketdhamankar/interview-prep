from collections import deque
from typing import Optional, List


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bfs_recursive(root: Optional[Node]):
    def bfs_recursive_helper(q: Optional[deque], ans: List[int]):
        if not q:
            return

        cur = q.popleft()
        if cur:
            ans.append(cur.val)
            q.append(cur.left)
            q.append(cur.right)
        bfs_recursive_helper(q, ans)
        return

    q = deque([root])
    output = []
    bfs_recursive_helper(q, output)
    return output

root = Node(4)
root.left = Node(9)
root.right = Node(0)
root.left.left = Node(5)
root.left.right = Node(1)

print(f'Recursive BFS: {bfs_recursive(root)}')