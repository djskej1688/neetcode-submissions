class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        ## 철자 비교
        arr = [0] * 26
        for ch in s:
            arr[ord(ch) - ord('a')] += 1
        
        for ch in t:
            arr[ord(ch) - ord('a')] -= 1
        
        for v in arr:
            if v != 0:
                return False
        return True 