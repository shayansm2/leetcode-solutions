/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    return {
        toBe: function(number) {
            if (val === number) {
                return true;
            }
            throw "Not Equal";
        },
        notToBe: function(number) {
            if (val !== number) {
                return true;
            }
            throw "Equal";
        },
    }
};