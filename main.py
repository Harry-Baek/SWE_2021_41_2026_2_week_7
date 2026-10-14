from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {}

    for i in range(len(nums)):
        num = nums[i]
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return []
