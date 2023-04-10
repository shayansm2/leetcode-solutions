/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
    let stack = [];
    for (let i = 0; i < s.length; i++) {
        let lastElement = stack.length > 0 ? stack[stack.length - 1] : undefined;

        if (s[i] === ')' && lastElement === '(') {
            stack.pop()
        } else if (s[i] === '}' && lastElement === '{') {
            stack.pop()
        } else if (s[i] === ']' && lastElement === '[') {
            stack.pop()
        } else {
            stack.push(s[i])
        }
    }

    return stack.length === 0
};