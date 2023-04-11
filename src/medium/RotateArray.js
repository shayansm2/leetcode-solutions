/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function (nums, k) {
    let covered = new Array(nums.length).fill(false);

    for (let i = 0; i < nums.length; i++) {
        if (covered[i]) {
            continue;
        }

        let curIndex = i;
        let curValue = nums[i];

        do {
            let j = (curIndex + k) % nums.length;
            let temp = curValue;
            curValue = nums[j];
            nums[j] = temp;
            covered[j] = true;
            curIndex = j;
        } while (curIndex !== i)
    }
};