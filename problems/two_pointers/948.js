// problem: bag of tokens
// link: https://leetcode.com/problems/bag-of-tokens/
// Difficulty: Medium

// Description: we have initial starting power and list of tokens
// and we start with score = 0. 
// we have to return maximum value of score.
// // rules are:
// face-up(score = 0): we can decrease our power in exchange of 1 score
// face-down(score = 1): we can increase our power in exchange of [..] power 

// Aproach: sort the array to keep track of cheapest and most expensive token
// use greedy aproach choosing the locally best available move 
// instead of trying every possible combination.

const tokens = [100, 200, 300, 400];
let power = 200;

// sort to use two pointers
tokens.sort((a,b) => a-b);
// cheapest
let left = 0;
// expensive
let right = tokens.length - 1;
// current score
let score = 0;
function bagOfTokens(tokens, power) {
    while (left <= right) {
        // if we have enough power to buy cheapest token
        if (power >= tokens[left]) {
            // we buy it and update current power
            power = power - tokens[left];
            // score + 1
            score++;
            // move on cuz we bought it already
            left++;
            // my solution was keeping failing because i was missing
            // left < right statement also which means
            // before playing face-down at least two tokens remain:
            } else if (score >= 1 && left < right) {
                // buy most expensive one
                power = power + tokens[right];
                // score - 1
                score--;
                // move inwards to the direction of cheapest
                right--;
            // i added this cuz in one of leetcodes test cases
            // the description said the if we have initial power
            // smaller than tokens[0] we return 0.  
            } else {
                break
        }
    }
    return score
}

const result = bagOfTokens(tokens, power);
console.log(result)


