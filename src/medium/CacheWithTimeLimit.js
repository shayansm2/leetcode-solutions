var TimeLimitedCache = function () {
  this.cache = {};
  this.promiseIds = {};
  this.promises = [];
};

/**
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function (key, value, duration) {
  let result = key in this.cache;
  this.cache[key] = value;
  let promiseId = this.promises.length;
  this.promises.push(
    new Promise(() =>
      setTimeout(() => {
        if (promiseId === this.promiseIds[key]) {
          delete this.cache[key];
        }
      }, duration)
    )
  );
  this.promiseIds[key] = promiseId;
  return result;
};

/**
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function (key) {
  if (!(key in this.cache)) return -1;
  return this.cache[key];
};

/**
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function () {
  return Object.keys(this.cache).length;
};

const timeLimitedCache = new TimeLimitedCache();
// console.log(timeLimitedCache.set(1, 42, 100)); // false
// setTimeout(() => {
//   console.log(timeLimitedCache.get(1)); // 42
//   console.log(timeLimitedCache.count()); // 1
// }, 50);

// setTimeout(() => {
//   console.log(timeLimitedCache.get(1)); // 42
//   console.log(timeLimitedCache);
// }, 150);
console.log(timeLimitedCache.set(1, 42, 50));
console.warn(timeLimitedCache);
setTimeout(() => {
  console.log(timeLimitedCache.set(1, 50, 100));
  console.warn(timeLimitedCache);
}, 40);
setTimeout(() => {
  console.log(timeLimitedCache.get(1));
  console.warn(timeLimitedCache);
}, 50);
setTimeout(() => {
  console.log(timeLimitedCache.get(1));
  console.warn(timeLimitedCache);
}, 120);
setTimeout(() => {
  console.log(timeLimitedCache.get(1));
  console.warn(timeLimitedCache);
}, 200);
setTimeout(() => {
  console.log(timeLimitedCache.count());
}, 250);
