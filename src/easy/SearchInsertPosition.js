/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function (nums, target) {
    let low = 0;
    let high = nums.length - 1;

    while (low <= high) {
        let mid = Math.floor(low + (high - low) / 2);

        console.log(low, mid,high);

        if (nums[mid] === target) {
            return mid;
        }

        if (nums[mid] < target) {
            low = mid + 1;
            continue;
        }

        high = mid - 1;
    }

    console.log(low,high);

    // this is the only difference from normal binary search algorithm
    return (nums[low] < target) ? low + 1 : low;
};