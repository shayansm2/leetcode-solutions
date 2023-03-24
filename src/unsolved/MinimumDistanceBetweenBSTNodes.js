// Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}

/**
 * @param {TreeNode} root
 * @return {number}
 */
var minDiffInBST = function (root) {
    let minDistance = undefined;
    let queue = [root];

    while (queue.length > 0) {
        let node = queue.pop();

        if (node.left) {
            queue.push(node.left);
            let dif = node.val - node.left.val;
            if (minDistance === undefined || dif < minDistance) {
                minDistance = dif;
            }
        }

        if (node.right) {
            queue.push(node.right);
            let dif = node.right.val - node.val;
            if (minDistance === undefined || dif < minDistance) {
                minDistance = dif;
            }
        }
    }

    return minDistance;
};
