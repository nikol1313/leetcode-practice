// Problem: remove dublicates from sorted array. 
// Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
// Difficulty: Easy




// description: 
// we have sorted list, we have to remove the duplicates and add _ in the end
// for how many duplicates we have. function should return k and nums list
// k = how many number we have, and nums the whole list with duplicates remove-duplicates-from-sorted-array


// aproach: because its sorted list the solution gonnabe easy , 
// we will need two points one going thru whole list and second one
// just capturing the unique ones and keeping track of position. 


function removeDupl(nums) {
    if (nums.length === 0) return 0;

    // pointer to keep track of unique nums
    let k = 1;
    // loop thru list
    for (let i = 1; i < nums.length; i++) {
        // if current number is not same as last number, 
        // meaning if we find unique num
        if (nums[i] !== nums[k - 1]) {
            // we replace current position of k with that num
            nums[k] = nums[i];
            // keep moving
            k++;
        }
    }
    
    return k;
}

let nums = [1, 1, 2];

let k = removeDupl(nums);

console.log(k); 
