/**
 * @param {number[]} num
 * @param {number} k
 * @return {number[]}
 */
var addToArrayForm = function (num, k) {
    let num2 = [...(String(k))];

    num = num.reverse();
    num2 = num2.reverse();

    for (let i = 0; i < num2.length; i++) {
        if (num[i] === undefined) {
            num.push(0);
        }

        num[i] += parseInt(num2[i]);
    }

    let carry = 0;
    for (let i = 0; i < num.length || carry > 0; i++) {
        if (num[i] === undefined) {
            num.push(0);
        }

        num[i] += carry;
        carry = 0;

        if (num[i] > 9) {
            carry = Math.floor(num[i] / 10);
            num[i] %= 10;
        }
    }

    return num.reverse();
};