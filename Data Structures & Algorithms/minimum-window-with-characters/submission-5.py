class Solution:
    def minWindow(self, s: str, t: str) -> str:
        curr, target = {}, {}


        subStringIndex, subStringLen = [-1, -1], float("infinity")

        # Create target conditions.
        for c in t:
            print("in tar loop")
            target[c] = 1 + target.get(c, 0)
        
        currConditions, neededConditions = 0, len(target)
        L = 0
        
        for R in range(len(s)):
            c = s[R] ## curr char
            curr[c] = 1 + curr.get(c, 0)

            if c in target and curr[c] == target[c]:
                currConditions += 1

            while currConditions == neededConditions:
                ## update possible output
                if (R - L + 1) < subStringLen:
                    subStringIndex = [L, R]
                    subStringLen = R - L + 1

                curr[s[L]] -= 1
                if s[L] in target and curr[s[L]] < target[s[L]]:
                    currConditions -= 1
                L += 1

        L, R = subStringIndex
    
        return s[L : R + 1] if subStringLen != float("infinity") else ""


        '''
        we need a sliding window, keep track of L and R pointers, move R until we meet
        conditions: "our pointers create a substring where we have every character in 't'"

        to find the smallest substring, once we meet conditions (have all chars in t),
        we move L pointer until we don't meet conditions, move R until we meet conditions
        again and compare with prev substring (take smaller substring)

        do this until R is null (out of bounds). R > len(s).

        To keep track of conditions:
            hashmaps for our current substring conditions and the target conditions.

            target hashmaps holds <char, freq> KV pair. 
                ex. if t = "XYZ", target = {"X" : 1, "Y" : 1, "Z" : 1}

            while iterating R (moving R by one index), check if s[R] in target, if so, add       
            to curr. compare curr[R] >= target, if so, need += 1.
        '''
