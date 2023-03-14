// Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}

function TreeStat(isValid, max, min) {
    this.isvalid = isValid;
    this.max = max;
    this.min = min;
}

/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function (root) {
    return getBSTStat(root).isvalid;
};

/**
 * @param {TreeNode} root
 * @return {TreeStat}
 */
function getBSTStat(root) {
    let isValid = true;
    let min = root.val;
    let max = root.val;

    if (root.left) {
        let leftStat = getBSTStat(root.left);

        min = Math.min(min, leftStat.min);
        max = Math.max(max, leftStat.max);

        isValid = isValid && leftStat.isvalid && (leftStat.max < root.val);
    }

    if (root.right) {
        let rightStat = getBSTStat(root.right);

        min = Math.min(min, rightStat.min);
        max = Math.max(max, rightStat.max);

        isValid = isValid && rightStat.isvalid && (rightStat.min > root.val);
    }

    return new TreeStat(isValid, max, min);
}
