class Solution:
    def firstUniqChar(self, s: str) -> int:
       count = Counter(s)
       for idx , no in enumerate(s):
        if count[no] == 1:
            return idx
       return -1
