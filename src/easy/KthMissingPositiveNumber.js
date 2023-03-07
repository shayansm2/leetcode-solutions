/**
 * @param {number[]} arr
 * @param {number} k
 * @return {number}
 */
var findKthPositive = function (arr, k) {
    if (k < arr[0]) {
        return k;
    }

    let len = arr.length

    let missingInBetween = (arr[len - 1] - arr[0] + 1) - len;

    if (k > missingInBetween + (arr[0] - 1)) {
        return arr[len - 1] + (k - arr[0] - missingInBetween + 1);
    }

    return BinarySearchKthPositive(arr, 0, len - 1, k - arr[0] + 1);
};

/**
 * @param {number[]} arr
 * @param {number} start
 * @param {number} end
 * @param {number} k
 * @return {number}
 */
function BinarySearchKthPositive(arr, start, end, k) {
    // breaking conditions
    // both start and end are inclusive

    let middleIndex = Math.floor((end - start) / 2) + start

    if (middleIndex === start) {
        return arr[start] + k;
    }

    let missingInFirstHalf = (arr[middleIndex] - arr[start]) - (middleIndex - start);

    if (k > missingInFirstHalf) {
        return BinarySearchKthPositive(arr, middleIndex, end, k - missingInFirstHalf);
    }

    return BinarySearchKthPositive(arr, start, middleIndex, k);
}