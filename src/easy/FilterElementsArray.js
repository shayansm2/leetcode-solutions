/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
  const result = [];
  arr.forEach((element, index) => {
    if (Boolean(fn(element, index))) {
      result.push(element);
    }
  });
  return result;
};

console.log(filter([0,10,20,30], function greaterThan10(n) { return n > 10; }));
console.log(filter([1,2,3], function firstIndex(n, i) { return i === 0; }));
console.log(filter([-2,-1,0,1,2], function plusOne(n) { return n + 1 }));
