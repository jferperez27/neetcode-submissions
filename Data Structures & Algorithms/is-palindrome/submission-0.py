class Solution:
    def isPalindrome(self, s: str) -> bool:
        txt = "".join(char.upper() for char in s if char.isalnum())

        index = len(txt) - 1

        for char in txt:
            if char != txt[index]:
                return False
            index -= 1
        return True