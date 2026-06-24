class Solution(object):
    def containsDuplicate(self, nums):
        new = list(set(nums))
        lennum = len(nums)
        lennew = len(new)

        # 1. Use "==" to compare, not "=" which assigns values
        if lennum == lennew:
            return False  # 2. Capitalize False
        else:
            return True  # 3. Capitalize True and remove the extra ":"

        ## or return len(nums) != len(set(nums))
