class Solution(object):
    def checkDivisibility(self, n):
        temp = n
        digitsum = 0
        digitproduct = 1

        while temp > 0:
            digit = temp % 10

            digitsum += digit
            digitproduct *= digit
            temp //= 10
        total = digitsum + digitproduct
        return n % total == 0