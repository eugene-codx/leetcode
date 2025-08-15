class Solution:
    # My solution
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        trg_dict = {k:v for v, k in enumerate(nums)}

        for i in range(len(nums)):
            res = target - nums[i]
            if res in trg_dict.keys() and i != trg_dict[res]:
                return [i, trg_dict[res]]
        return [-1, -1]

    def twoSum_gpt5(self, nums: list[int], target: int) -> list[int]:
        lookup = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in lookup:
                return [lookup[diff], i]
            lookup[num] = i
        return [-1, -1]

a = Solution()
print(a.twoSum([1, 22, 33, 3], 34))
