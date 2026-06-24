class Solution(object):
    def twoSum(self, nums, target):
        arr = [(num, idx) for idx, num in enumerate(nums)]
        arr.sort(key=lambda x: x[0])

        left, right = 0, len(arr) - 1

        while left < right:
            curr_sum = arr[left][0] + arr[right][0]

            if curr_sum == target:
                return [arr[left][1], arr[right][1]]
            elif curr_sum < target:
                left += 1
            else:
                right -= 1


# hash map solution
""" def twoSum(nums, target):
    mp = {}

    for i, x in enumerate(nums):
        diff = target - x

        if diff in mp:
            return [mp[diff], i]

        mp[x] = i"""
