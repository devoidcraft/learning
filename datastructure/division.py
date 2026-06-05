class Solution(object):
    def divide(self, dividend, divisor):

        if divisor == 0:
            return 0

        # handle overflow case
        if dividend == -(2**31) and divisor == -1:
            return 2**31 - 1

        # sign logic
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        i = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1

            # double divisor until it exceeds dividend
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend -= temp
            i += multiple

        return sign * i
