// Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}

/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isCompleteTree = function (root) {
    let queue = [root];
    let levels = [0];
    let positions = ['left'];
    let hashMap = new Map();
    let stack = [];

    while (queue.length > 0) {
        let node = queue.shift();
        let level = levels.shift();
        let position = positions.shift();

        let count = hashMap.get(level);

        if (count === undefined) {
            hashMap.set(level, 1);
        } else {
            hashMap.set(level, count + 1);
        }

        let isLeaf = true;

        if (node.left) {
            queue.push(node.left);
            levels.push(level + 1);
            positions.push('left');
            isLeaf = false;
        }

        if (node.right) {
            queue.push(node.right);
            levels.push(level + 1);
            positions.push('right');
            isLeaf = false;
        }

        if (isLeaf) {
            if (position === 'right' && stack.length > 0 && stack[stack.length - 1] === 'left') {
                stack.shift();
            } else {
                stack.push(position)
            }
        }
    }

    for (let [key, value] of hashMap) {
        if (hashMap.size === key) {
            break;
        }

        if (Math.pow(2, key) !== value) {
            return false;
        }
    }

    if (stack.length > 1) {
        return false;
    }

    if (stack.length === 1 && stack[0] === 'right') {
        return false;
    }

    return true;
};