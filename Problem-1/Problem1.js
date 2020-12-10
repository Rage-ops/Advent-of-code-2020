// Advent of Code 2020 Day 1

const fs = require('fs');
const data = fs.readFileSync('./Problem-1.txt').toString().split('\n');
const arr = data.map((val) => Number(val));

const solution = (array, target) => {
    let left = 0, right = array.length - 1;
    while (left < right){
        if (array[left] + array[right] === target){
            return [left, right];
        }
        else if (array[left] + array[right] < target){
            left++;
        }
        else{
            right--;
        }
    }
}

const part1 = (arr) => {
    return solution(arr.sort(), 2020).reduce((acc, index) => {
        return acc * arr[index];
    }, 1)
};

console.log(part1(arr));

const hash_map = {}
arr.forEach((val, index)=>{
    hash_map[val] = index;
});
const partTwo = (array, target) => {
    for(i in hash_map){
        let b = target - i;
        const res = solution(array, target - i);
        if (res !== undefined){
            if(res[0] !== array[i] && res[1] !== array[i]){
                return i * array[res[0]] * array[res[1]];
            }
        }
    }
}
console.log(partTwo(arr.sort(), 2020));