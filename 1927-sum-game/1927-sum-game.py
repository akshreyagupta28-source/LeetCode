class Solution(object):
    def sumGame(self, num):
        n = len(num) // 2

        left_sum = 0
        right_sum = 0
        left_q = 0
        right_q = 0

        for i in range(n):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])

        for i in range(n, len(num)):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])

        if (left_q + right_q) % 2 != 0:
            return True

        return 9 * (left_q - right_q) != 2 * (right_sum - left_sum)