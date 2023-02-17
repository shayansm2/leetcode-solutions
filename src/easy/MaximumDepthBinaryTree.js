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
var maxDepth = function (root) {
    if (!root) {
        return 0;
    }

    let queue = [root];
    let depths = [1];
    let maxDepth = 0;

    while (queue.length > 0) { // Thanks to ChatGPT
        let node = queue.pop();
        let nodeDepth = depths.pop();

        if (maxDepth < nodeDepth) {
            maxDepth = nodeDepth;
        }

        if (node.left) {
            queue.push(node.left);
            depths.push(nodeDepth + 1);
        }

        if (node.right) {
            queue.push(node.right);
            depths.push(nodeDepth + 1);
        }
    }

    return maxDepth;
};