class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Permutations：
        size = len(nums)
        for i in range(0, size, 1):
            for y in range(i + 1, size, 1):
                if nums[i] + nums[y] == target:
                    return [i, y]

        # 2 passes hash table:
        numToIndex = []
        for i in range(0, len(nums), 1):
            if target - nums[i] in numToIndex:
                return [numToIndex[target - nums[i]], i]
            numToIndex[nums[i]] = i
