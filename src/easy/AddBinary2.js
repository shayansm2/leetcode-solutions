/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function (a, b) {
    a = getReversedArray(a);
    b = getReversedArray(b);

    let result = [];

    for (let i = 0; i < Math.max(a.length, b.length); i++) {
        result.push(getNumberFromString(a[i]) + getNumberFromString(b[i]));
    }

    let carry = 0;
    for (let i = 0; i < result.length; i++) {
        if (carry) {
            result[i] += carry;
            carry = 0;
        }

        if (result[i] < 2) {
            continue;
        }

        carry = Math.floor(result[i] / 2);

        console.log('carry', carry);

        result[i] = result[i] % 2;
    }

    while (carry) {
        result.push(carry % 2);
        carry = Math.floor(carry / 2);
    }

    return getReversedString(result);
};

/**
 * @param {string} str
 * @returns {[]}
 */
function getReversedArray(str) {
    return [...str].reverse();
}

/**
 * @param {[]} array
 * @returns {String}
 */
function getReversedString(array) {
    return array.reverse().join("")
}

/**
 * @param {string} str
 * @returns {number}
 */
function getNumberFromString(str) {
    if (str === undefined) {
        return 0;
    }

    return parseInt(str);
}