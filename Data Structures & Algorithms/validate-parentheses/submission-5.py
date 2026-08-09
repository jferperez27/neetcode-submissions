class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []
        for n in s:
            if n not in closeToOpen:
                stack.append(n)
            else:
                if len(stack) > 0:
                    curr = stack.pop()
                    if curr != closeToOpen[n]:
                        return False
                    continue
                return False
        if len(stack) != 0:
            return False
        return True
