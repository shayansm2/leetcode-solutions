/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
  let result = [];
  arr.forEach((element, index) => {
    result.push(fn(element, index));
  });
  return result;
};

console.log(map([1,2,3], n=>n+1));
console.log([1,2,3].map(n=>n+1));

console.log(map([1,2,3], (n,i)=>n+i));
console.log([1,2,3].map((n,i) => n+i))

console.log(map([1,2,3], function constant() { return 42; }));
console.log([1,2,3].map(()=>42))