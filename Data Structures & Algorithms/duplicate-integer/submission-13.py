class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            copied = nums.copy()
            n = copied.pop(i)

            for j in copied:
                if n == j:
                    return True

        return False
