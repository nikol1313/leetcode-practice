// Problem: Two sum 2
// link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
// Difficulty: Medium


// Description: find the two nums that add up to target in a sorted list
// in where: 1 <= index1 < index2 <= numbers.length. 

// aproach: my aproach was classica two pointers and i only needed 2 tries
// to solve this problem , it should be easy instead of medium lol.

const numbers = [2,7,11,15]
const target = 9

function twoSum(numbers, target) {
    // define pointers
    let num1 = 0;
    let num2 = numbers.length - 1;
    // until they collied
    while(num1 < num2) {
        // if sum is bigger decrease
        if (numbers[num1] + numbers[num2] > target) {
            num2--;
        // if sum is smaller increase
        } else if (numbers[num1] + numbers[num2] < target) {
            num1++;
        } else { 
            // return the indexes (+1 because the list starts from 0)
            // and leetcode wanted to return exact indexes 
            return [num1+1, num2+1]
            // once we find we just end the function
            break;
        }
    }
}

const res = twoSum(numbers, target)
console.log(res)



