class Solution(object):
    def maxIceCream(self, costs, coins):
        count = 0
        costs.sort()
        for num in costs:
            if coins<num:
                break
            count+=1
            coins -= num
        return count

        