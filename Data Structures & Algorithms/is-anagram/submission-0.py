class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        visited0 = {}
        visited1 = {}
        if len(s) != len(t):
            return False
        else:
            for char in list(s):
                if char in visited0:
                    visited0[char] += 1
                else:
                    visited0[char] = 1
            for char in list(t):
                if char in visited1:
                    visited1[char] += 1
                else:
                    visited1[char] = 1
            if visited0.items() == visited1.items():
                return True
            else:
                return False