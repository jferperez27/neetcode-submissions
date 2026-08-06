class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            l = str(len(s))
            output += l + "#" + s
        print(output)
        return output


    def decode(self, s: str) -> List[str]:
        output = []
        currInt = 0
        currString = ""
        string = ""
        counting = False
        for c in s:
            if c.isdigit() and not counting:
                currString += c
                continue
            if c == "#" and not counting:
                curr = int(currString)
                if curr == 0:
                    output.append(string)
                    string = ""
                    continue
                else:                 
                    counting = True
                    continue
            if counting:
                string += c
                curr -= 1
                if curr == 0:
                    output.append(string)
                    counting = False
                    string = ""
                    currString = ""
                    continue

        return output