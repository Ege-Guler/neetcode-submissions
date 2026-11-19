from collections import Counter 

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len, s2_len = len(s1), len(s2)
        if s1_len > s2_len:
            return False

        count_s1 = Counter(s1)

        left = 0

        count_s2 = Counter(s2[0:s1_len])

        if count_s2 == count_s1:
            return True


        for right in range(s1_len, s2_len):
            count_s2[s2[right]] = count_s2.get(s2[right], 0) + 1

            count_s2[s2[left]] -= 1
            if count_s2[s2[left]] == 0:
                del count_s2[s2[left]]
            left += 1

            if count_s2 == count_s1:
                return True

        return False            