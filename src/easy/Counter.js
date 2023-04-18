/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function (n) {
    this.n = n;
    return function () {
        this.n++;
        return this.n - 1;
    };
};


const counter = createCounter(10)
counter() // 10
counter() // 11
counter() // 12
