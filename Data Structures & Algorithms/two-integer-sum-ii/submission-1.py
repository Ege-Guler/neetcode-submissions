class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i, j = 0, len(numbers) - 1

        while numbers[i] + numbers[j] != target:

            two_sum = numbers[i] + numbers[j]


            if  two_sum > target:
                j-= 1

            elif two_sum < target:
                i += 1
        
        return [i + 1, j + 1]