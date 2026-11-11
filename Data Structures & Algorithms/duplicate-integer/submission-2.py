from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = Counter(nums)
        for i,j in dic.items():
            if j > 1:
                return True
        return False
        