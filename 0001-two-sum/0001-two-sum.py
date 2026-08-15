class Solution:
    def twoSum(self, nums, target):
        arr = []

        for i in range(len(nums)):
            arr.append((nums[i], i))

        
        arr.sort()

        start = 0
        end = len(arr) - 1

        while start < end:

    
            sum = arr[start][0] + arr[end][0]

            if sum == target:
                return [arr[start][1], arr[end][1]]

            elif sum > target:
                end -= 1

            else:
                start += 1

        return []