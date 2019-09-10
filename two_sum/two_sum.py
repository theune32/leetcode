from typing import List


# first implementation, simple attempt
class Solution:
    @staticmethod
    def two_sum_brute_force(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    @staticmethod
    def two_pass_hash_table(nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(0, len(nums)):
            map[nums[i]] = i
        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in map and map.get(complement) is not i:
                return [i, map.get(complement)]

    @staticmethod
    def one_pass_hash_table(nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in map:
                return [map.get(complement), i]
            map[nums[i]] = i
