class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            rest = nums[:i] + nums[i+1:]

            for j in rest:
                if nums[i] - j == 0:
                    return True

        return False