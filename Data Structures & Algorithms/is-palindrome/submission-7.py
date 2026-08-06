class Solution:
    def isPalindrome(self, s: str) -> bool:
        txt = "".join(char.upper() for char in s if char.isalnum())

        right = len(txt) - 1
        for char in txt:
            if char != txt[right]:
                return False
            right -= 1
        return True