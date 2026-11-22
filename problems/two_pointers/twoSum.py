# TwoSum
# Link: https://leetcode.com/problems/two-sum/description/
# Difficulty: Easy

# Description:
# we need to find 2 numbers that add up to the target number and return their indexes.

# Thought Process:
# first one that came to my mind was the worst solution because it means pairing every number
# with each other that takes too much resources.

# Code:
nums = [2,7,11,15]
target = 9

def TwoSum(num_list: list[int], target_num: int) -> list[int]:
    for i in range(len(num_list)):
        for y in range(i+1, len(num_list)):
            if num_list[i] + num_list[y] == target_num:
                return [i , y]
    return None

print(TwoSum(nums ,target))

# better solution than this is taking the current number

