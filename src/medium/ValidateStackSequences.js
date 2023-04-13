/**
 * @param {number[]} pushed
 * @param {number[]} popped
 * @return {boolean}
 */
var validateStackSequences = function (pushed, popped) {
    let stack = [];
    let i = 0;
    let j = 0;

    while (true) {
        if (j < popped.length && stack.length > 0 && stack[stack.length - 1] === popped[j]) {
            stack.pop();
            j++;
            continue;
        }

        if (i >= pushed.length) {
            break;
        }

        stack.push(pushed[i]);
        i++;
    }

    return stack.length === 0;
};