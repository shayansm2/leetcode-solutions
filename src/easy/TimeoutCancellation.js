/**
 * @param {Function} fn
 * @param {Array} args
 * @param {number} t
 * @return {Function}
 */
var cancellable = function (fn, args, t) {
  let canceled = false;
  setTimeout(() => {
    if (!canceled) fn(args);
  }, t);
  return () => (canceled = true);
};

const fn = (x) => x * 5;
const args = [2],
  t = 100,
  cancelTimeMs = 50;

const start = performance.now();
const logs = [];
const log = (...argsArr) => {
  const diff = Math.floor(performance.now() - start);
  logs.push({ time: diff, returned: fn(...argsArr) });
};

const cancel = cancellable(log, args, t);

setTimeout(cancel, cancelTimeMs);

setTimeout(() => {
  console.log(logs); // [{"time":20,"returned":10}]
}, Math.max(t, cancelTimeMs) + 15);
