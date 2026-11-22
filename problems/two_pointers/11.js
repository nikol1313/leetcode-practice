// Problem: containers with water 
// link: https://leetcode.com/problems/container-with-most-water/

// description: we need to find the are betwen two numbers (walls)
// that can hold the largest amount of water
// to calculate distance we nee distance between two numbers and the
// shortest number between two numbers, because the water will spill
// if we pick the biggest

// aproach: the techinque is two pointers but my first try was
// bad, because i was using for loop instead of manually movable
// pointer, so after visualizing the workflow, i came to this solution


const nums= [1,8,6,2,5,4,8,3,7]
function biggestWater(nums) {
    // take the last element
    let left = 0;
    let right = nums.length - 1;
    // the result container
    let result = 0;
    // loop thru list until we reach middle part
    while (left < right) {
        // calculate distance
        let width = right - left;
        // we need to pick shortest because,
        // if we pick biggest the water is gonna spill
        let min = Math.min(nums[left], nums[right])
            //  if current area is bigger than result we update it.
            if ((width * min) > result) {
                result = width * min;
            }
            // if left one is shorter we move on next wall
            if (nums[left] < nums[right]) {
                left++;
            }
            // and if right one is bigger we go to the left side
            else (right--)
    }
    return result
}

const result = biggestWater(nums)
console.log(result)
