import heapq

class Solution:

    #  0  1  2  3
    # [0, 0, 1, 3]
    #
    #   0     3
    #   1
    #   2
    def find(self, parent, x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(self, parent, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        
        if root_x == root_y:
            return
        parent[root_x] = root_y

    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0: return 0
        
        parent = list(range(len(nums))) #[0, 1, 2, 3]
        nums_set = set()
        num_to_index = {num: i for i, num in enumerate(nums)}

        for num in nums:
            nums_set.add(num)
        
        for num in nums:
            if num + 1 in nums_set:
                self.union(parent, num_to_index[num], num_to_index[num + 1])

        groups = {}
        for i in range(len(nums)):
            root = self.find(parent, i)
            groups.setdefault(root, []).append(nums[i])
        return len(max(groups.values(), key=len))
