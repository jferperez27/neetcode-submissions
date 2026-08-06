class Solution:
    def isPalindrome(self, s: str) -> bool:
        txt = "".join(char.upper() for char in s if char.isalnum())

        index = len(txt) - 1
        for left in range(len(txt) - 1):
            if txt[left] != txt[index]:
                return False
            elif left == index:
                return True
            index -= 1
        return True