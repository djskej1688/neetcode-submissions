class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #1. O(n^2) : O(n)으로 순회하면서 target을 그 값의 -로 보면 됨. O(n)에 Two Pointer로
        ans = []
        nums.sort()
        if nums.count(0) >= 3 : # count 3
            ans += [[0, 0, 0]]
        s = set(nums)
        for k in range(len(nums)):
            if k < len(nums) - 1 and nums[k + 1] == nums[k]:
                continue
            if k >= 1 and nums[k - 1] == nums[k] and nums[k] != 0:
                if -2 * nums[k] in s:
                    ans += [[nums[k], nums[k], -2 * nums[k]]]
            target = -nums[k]
            l, r = k + 1, len(nums) - 1
            while l < r :
                while l + 1 <= len(nums) - 1 and nums[l] == nums[l + 1] :
                    l += 1
                while r - 1 >= k + 1 and nums[r] == nums[r - 1]:
                    r -= 1
                if l >= r :
                    break
                if nums[l] + nums[r] == target:
                    ans += [[-target, nums[l], nums[r]]]
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return ans 