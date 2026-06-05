class Solution(object):
    def romanToInt(self, s):
        int_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        integer = 0

        for i in range(len(s) - 1):
            if int_map[s[i]] < int_map[s[i + 1]]:
                integer -= int_map[s[i]]
            else:
                integer += int_map[s[i]]

        integer += int_map[s[-1]]
        return integer
