from typing import Optional, List


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Solution:
    def inorderSuccessor(self, root: Node, key: int) -> Optional[int]:
        if not root:
            return None

        succ = None
        while root:
            if root.data < key:
                root = root.right
            elif root.data > key:
                succ = root.data
                root = root.left
            else:
                if root.right:
                    succ = self.inorderSuccessor(root, key)
                break

            if root is None:
                return succ
        return succ


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

ans = s.inorderSuccessor(root, 2)
print(ans)
