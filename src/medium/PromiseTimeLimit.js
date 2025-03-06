/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function (fn, t) {
  return async function (...args) {
    return Promise.race([
      new Promise((resolve) => resolve(fn(...args))),
      new Promise((_, reject) =>
        setTimeout(() => reject("Time Limit Exceeded"), t)
      ),
    ]);
  };
};

// let t = 100;
// let fn = (t) => new Promise((res) => setTimeout(res, t));
// const limited = timeLimit(fn, t);
// limited(150).then(console.log).catch(console.log); // "Time Limit Exceeded" at t=100ms
//----------------------------------------------------------------------------------------------------
const fn = async (n) => {
  await new Promise((res) => setTimeout(res, 100));
  return n * n;
};
const inputs = [5];
const t = 50;
const limited = timeLimit(fn, t);
const start = performance.now();
let result;
try {
  const res = await limited(...inputs);
  result = { resolved: res, time: Math.floor(performance.now() - start) };
} catch (err) {
  result = { rejected: err, time: Math.floor(performance.now() - start) };
}
console.log(result); // Output
