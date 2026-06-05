class Solution(object):
    def multiply(self, num1, num2):
        def converter(s):
            result = 0
            for ch in s:
                digit = ord(ch) - ord("0")  # convert char to digit
                result = result * 10 + digit
            return result

        def int_to_string(num):
            if num == 0:
                return "0"
            result = ""

            while num > 0:
                digit = num % 10
                ch = chr(digit + ord("0"))  # convert digit → char
                result += ch
                num //= 10

            return result[::-1]  # reverse string

        answer = converter(num1) * converter(num2)
        new = int_to_string(answer)

        return new
