/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function (a, b) {
    let output = '';
    let carry = false;

    let length = Math.max(a.length, b.length);
    a = getReversedString(a);
    b = getReversedString(b);

    for (let i = 0; i < length; i++) {
        let bitA = getBoolFromStr(a[i])
        let bitB = getBoolFromStr(b[i])

        let add = fullAdder(bitA, bitB, carry);

        carry = add.carryOut
        output = (add.sum ? '1' : '0') + output;
    }

    while (carry) {
        let add = fullAdder(false, false, carry);

        carry = add.carryOut
        output = (add.sum ? '1' : '0') + output;
    }

    return output;
};

function getBoolFromStr(str) {
    if (str === undefined) {
        return false;
    }

    return str !== '0';
}

/**
 * @param {string} str
 */

function getReversedString(str) {
    return [...str].reverse().join("");
}

/**
 * @param {boolean} a
 * @param {boolean} b
 */
function halfAdder(a, b) {
    return {
        sum: a ^ b,
        carryOut: a & b
    };
}


/**
 * @param {boolean} a
 * @param {boolean} b
 * @param {boolean} carryIn
 */

function fullAdder(a, b, carryIn) {
    let firstSum = halfAdder(a, b);
    let secondSum = halfAdder(carryIn, firstSum.sum);
    return {
        sum: secondSum.sum,
        carryOut: firstSum.carryOut | secondSum.carryOut
    };
}
