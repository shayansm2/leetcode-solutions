/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    nums.forEach(element => {
        init = fn(init, element);
    });
    return init;
};

console.log(reduce([1,2,3,4], (accm, curr) => accm + curr, 0));
console.log([1,2,3,4].reduce((accm, curr) => accm+curr, 0));

console.log(reduce([1,2,3,4], function sum(accum, curr) { return accum + curr * curr; }, 100));
console.log([1,2,3,4].reduce((accm, curr) => accm + curr * curr, 100));

console.log(reduce([], function sum(accum, curr) { return 0; }, 25));
console.log([].reduce(()=>0, 25));