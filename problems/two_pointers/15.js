// Problem: 3sum
// Link: https://leetcode.com/problems/3sum/description/
// Difficulty: Medium

// description: we need to return list of numbers in where they add up to 0
// and every list should be unique.

// this is similar to two sum except theres 3 number and every solution should differ

// Aproach: i tried like 10 solutions on my own, none worked. gave up and
//  then i searched hints for this problems on stack overflow.
//  in the end i solved the whole problem after 1.30h+ 
//  explained each step with comments.




const nums = [-1,0,1,2,-1,-4];
function threeSum(nums) {
// sort the array to use two pointers on this problem
nums.sort((a,b) => a - b);
// container to store lists of unique nums that add up to 0
const result = [];

// "- 2" because Pick needs two spaces after it: one for L, one for R
for (let i = 0; i < nums.length - 2; i++) {
    // if the current number is positive we dont need it,
    // cuz array is sorted and there is no way its gonna get 0
    if (nums[i] > 0) break;
    // if the current number is same as previous we skip cuz
    // we dont need duplicates
    if (i > 0 && nums[i] === nums[i - 1]) continue;

    // we start with one more than current index
    let left = i + 1;
    let right = nums.length - 1;

    // until sides collide
    while (left < right) {
        // we want sum to be 0
        const sum = nums[i] + nums[left] + nums[right];
        // if bigger go left side
        if (sum > 0) {
            right--;
        // if smaller we go right side
        } else if (sum < 0) {
            left++;
        // once we find the desired list we push to our result container
        } else {
            result.push([nums[i], nums[left], nums[right]]);
            left++;
            right--;
            // this line prevent getting the same team again and again.
            // EXPLANATION DOWN 
            while (left < right && nums[left] === nums[left - 1]) left++;
            }
        }
    }
    return result
}

res = threeSum(nums);
console.log(res)


/*
 *  Why: while (left < right && nums[left] === nums[left - 1]) left++;
 *
 *  Example: [-2, 0, 0, 1, 2, 2]
 *  Pick = -2 ,  we need L + R = 2
 *
 *     -2   0   0   1   2   2
 *      P   L               R      0 + 2 = 2 → TEAM (-2, 0, 2)
 *
 *  After saving, we do left++ and right--:
 *
 *     -2   0   0   1   2   2
 *      P       L       R          L is on 0 AGAIN, meaning we need 2 again
 *                                 =  SAME team (-2, 0, 2) 
 *
 *  Why we DON'T need the same skip for R
 *
 *     -2   0   0   1   2   2
 *      P           L   R          L = 1 (new), R = 2 (copy of old R)
 *
 *  L moved to a BIGGER number, R stayed the same
 *   bigger L + same R = sum too big
*/ 
