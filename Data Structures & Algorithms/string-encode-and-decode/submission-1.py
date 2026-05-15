class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "*" + s

        return encoded_str

    def decode(self, s: str) -> List[str]:
        ans = []
        temp = ""

        i = 0
        length = len(s)
        while i<length:
            if(s[i] == "*"):
                ans.append(s[i + 1: i + int(temp) + 1])
                i += int(temp) + 1
                temp = ""
                continue
            temp += s[i]
            i+=1

        return ans