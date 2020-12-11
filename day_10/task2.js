const fs = require('fs')
const path = require('path');
const file = fs.readFileSync(path.resolve(__dirname, 'input.txt'));

const inputNums = file.toString().split('\n').map(elem => parseInt(elem));
let nums = [0, ...inputNums.sort((a, b) => a - b), Math.max(...inputNums) + 3];

let knownWays = Object();

function getNumberOfWaysToEndFromIndex(index) {
    if(knownWays[index] !== undefined) {
        return knownWays[index];
    } else {
        let ways = helper(index);
        knownWays[index] = ways;
        return ways;
    }
}

function helper(index) {
    if(index == nums.length - 1)
        return 1;
    if(index == nums.length - 2)
        return 1;
    if(index == nums.length - 3) {
        if(nums[nums.length - 1] - nums[index] <= 3) {
            return 2;
        } else {
            return 1;
        }
    }

    let numberOfWaysToEnd = 0;
    numberOfWaysToEnd += getNumberOfWaysToEndFromIndex(index + 1);
    if(nums[index + 2] - nums[index] <= 3) {
        numberOfWaysToEnd += getNumberOfWaysToEndFromIndex(index + 2);
    }
    if(nums[index + 3] - nums[index] <= 3) {
        numberOfWaysToEnd += getNumberOfWaysToEndFromIndex(index + 3);
    }
    return numberOfWaysToEnd;
}

console.log(getNumberOfWaysToEndFromIndex(0))
