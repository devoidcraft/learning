class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        hash_map = {}

        # count magazine characters
        for ch in magazine:
            hash_map[ch] = hash_map.get(ch, 0) + 1
            """If character exists → return its value
                If not → return 0
                Then:
                add 1"""

        # use characters for ransomNote
        for ch in ransomNote:
            if ch not in hash_map or hash_map[ch] == 0:
                return False
            hash_map[ch] -= 1

        return True
