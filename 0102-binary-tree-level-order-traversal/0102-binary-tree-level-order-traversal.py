import collections

class Solution:
    def levelOrder(self, root):
        res = []

        if not root:
            return res

        a = collections.deque()
        a.append(root)

        while a:
            a_len = len(a)
            level = []

            for i in range(a_len):
                node = a.popleft()
                level.append(node.val)

                if node.left:
                    a.append(node.left)

                if node.right:
                    a.append(node.right)

            res.append(level)

        return res