from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums or k <= 0:
            return []
        n = len(nums)
        result = []
        q = deque()
        for i in range(n):
            # Remove indices outside the window
            while q and q[0] < i - k + 1:
                q.popleft()
            # Remove smaller elements from the back
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            # Add current index
            q.append(i)
            # Window is complete
            if i >= k - 1:
                result.append(nums[q[0]])
        return result