class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""
        for s in strs:
            length = len(s)
            output = output + str(length) + "%" + s
        return output

    def decode(self, s: str) -> List[str]:
        output = []
        print(s)
        index = 0
        length = ""
        while index != len(s):
            curr = s[index]
            if curr == "%":
                output.append(s[index + 1 : index + 1 + int(length)])
                index += 1 + int(length)
                length = ""
                continue
            length += curr
            index += 1
        return output
            