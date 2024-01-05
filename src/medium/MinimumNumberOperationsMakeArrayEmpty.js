/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
    let occurance = {};
    for (i in nums) {
        let val = nums[i];
        if (val in occurance) {
            occurance[val]++
        } else {
            occurance[val] = 1
        }
    }
    let result = 0
    for (i in occurance) {
        let occur = occurance[i]
        if (occur == 1) {
            return -1
        }

        result += Math.floor(occur / 3)
        if (occur % 3) {
            result++
        }
    }
    return result
};