class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = defaultdict(int)
        t_map = defaultdict(int)

        for i, val in enumerate(s):
            s_map[val] +=1

        for i, val in enumerate(t):
            t_map[val] +=1

        if s_map.keys() == t_map.keys():
            for i in s_map.keys():
                if s_map[i] != t_map[i]:
                    return False
            return True
        return False