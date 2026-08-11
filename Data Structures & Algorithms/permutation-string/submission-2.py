class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)

        if len_s1 > len_s2 :
            return False

        chars = defaultdict(int)

        for c in s1:
            chars[c] += 1
        


        window = defaultdict(int)
        matches = 0
        left = 0

        for right, c in enumerate(s2):

            if c not in chars:
                window.clear()
                matches = 0
                left = right + 1
                continue
            else:
                window[c] += 1
                
                if window[c] == chars[c]:
                    matches += 1

                # too many
                elif window[c] == chars[c] + 1:
                    matches -= 1

                while right - left + 1 > len_s1:
                    out = s2[left]
                    window[out] -= 1
                    if window[out] == chars[out]:
                        matches += 1
                    elif window[out] == chars[out] - 1:
                        matches -= 1

                    left += 1
                
                if matches == len(chars) and right - left + 1 == len_s1:
                    return True

        return False


