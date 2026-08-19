class Solution:

    def encode(self, strs: List[str]) -> str:
        output = ""

        for s in strs:
            output += str(len(s)) + "%" + s

        return output


    def decode(self, s: str) -> List[str]:
        index = 0
        output = []

        while index != len(s):
            length = s[index]
            index += 1
            while s[index] != "%":
                length += s[index]
                index += 1

            print(length)
            
            output.append(s[index+1:index+int(length) + 1])

            index += int(length) + 1

        return output