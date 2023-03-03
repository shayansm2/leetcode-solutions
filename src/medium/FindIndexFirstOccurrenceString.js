/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function (haystack, needle) {
    let i = 0;
    let j = 0;

    while (j < haystack.length && i < needle.length) {
        if (haystack[j] === needle[i]) {
            i ++;
        } else {
            j -= i;
            i = 0;
        }

        j++;
    }

    return i === needle.length ? j - i : -1;
};