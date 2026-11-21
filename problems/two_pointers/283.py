# Problem: move zeroes
# Link: https://leetcode.com/problems/move-zeroes/
# Difficulty: Easy

# Problem:
# we have to move zeroes to the right while keeping the order.


# Aproach:
# my first thought was to first track the current number starting from left
# if that current nummber is 0 , we remove that num and append 0 to the front.
# but my logic had a lot of issue and it didnt work. after thinking carefully:

# correct solution needs two pointers one going over each index and 
# second one remembering which was 0
# and in the end when the loop ends we need to add those 0 the first loop remembered.


nums = [0, 1, 0, 3, 12]
# Output: [1,3,12,0,0]

def moveZeroes(self, nums: list[int]) -> None:
# define two pointers:
i = 0
j = 0
# program runs until we out of indexes
while i < len(nums):
    # if our current number is not 0
    if nums[i] != 0:
        # we use second pointer to remember that its non-zero num.
        nums[j] = nums[i]
        # we move on simoultenously.
        i += 1
        j += 1
    else:
        # here is the trick part, we only move on to the next number if
        # the current number is 0, so by iterating the "i", "j" stayes
        # the same meaning it remembered that theres zero on current indx.
        i += 1
# i understood previous code but didnt know how to add 0s to the list,
# so i used a hint, now it makes logical sense.

# when first loop ended we have 
#j = 3
#i = max indx.
# and now because we have j = 3 we can go until the last list index and replace with 0.
while j < len(nums):
    # replace with 0
    nums[j] = 0
    # move to next num.
    j += 1

return nums

# time complexity: O(n) 
