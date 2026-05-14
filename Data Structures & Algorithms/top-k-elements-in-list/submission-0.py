class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1
        freq_list = sorted(freq.items(), key=lambda x: x[1], reverse=True)[0:k]
        return [x[0] for x in freq_list]