from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s ==t and len(s)==1:
            return True
        if len(s) != len(t):
            return False

        d1 = Counter(s)
        d2 = Counter(t)
        return d1==d2

        

        