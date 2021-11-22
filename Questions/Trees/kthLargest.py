from typing import Optional, List


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def kth_largest(self, root: Optional[Node], k: int) -> int:
        def helper(cur: Optional[Node], visited_nodes: List[int]):
            if not cur:
                return None
            right = helper(cur.right, visited_nodes)
            if right is not None:
                return right
            visited_nodes[0] += 1
            if visited_nodes[0] == k:
                return cur.data
            return helper(cur.right, visited_nodes)

        visited_nodes = [0]
        return helper(root, visited_nodes)


# root = Node(5)
# root.left = Node(3)
# root.right = Node(6)
#
# root.left.left = Node(2)
# root.left.right = Node(4)
# root.left.left.left = Node(1)
#
# root.right.right = Node(8)
# root.right.right.left = Node(7)
# root.right.right.right = Node(9)
root = Node(3)
root.left = Node(0)
root.right = Node(16)
root.left.right = Node(2)
root.left.right.left = Node(1)
s = Solution()

ans = s.kth_largest(root, 2)
print(ans)
