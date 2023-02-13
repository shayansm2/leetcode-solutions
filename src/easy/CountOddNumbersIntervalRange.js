/**
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var countOdds = function(low, high) {
    let newHigh = parseInt(high/2);
    let newLow = parseInt(low/2);

    if (low % 2 === 1) {
        newLow += 1;
    }

    console.log(newHigh, newLow);

    return high - low - newHigh + newLow;
};