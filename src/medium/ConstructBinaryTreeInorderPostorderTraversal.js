// Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}

/**
 * @param {number[]} inorder
 * @param {number[]} postorder
 * @return {TreeNode}
 */

var buildTree = function (inorder, postorder) {
    console.log(inorder, postorder)

    if (inorder.length === 0) {
        return undefined;
    }

    if (inorder.length === 1) {
        if (JSON.stringify(inorder) === JSON.stringify(postorder)) {
            return new TreeNode(inorder[0]);
        } else {
            return null;
        }
    }

    if (inorder.length === 2) {
        if (JSON.stringify(inorder) === JSON.stringify(postorder)) {
            return new TreeNode(postorder[1], new TreeNode(postorder[0]));
        } else if (JSON.stringify(inorder.reverse()) === JSON.stringify(postorder)) {
            return new TreeNode(postorder[1], undefined, new TreeNode(postorder[0]));
        } else {
            return null;
        }
    }

    let rootVal = postorder[postorder.length - 1];

    for (let i = 0; i < inorder.length; i++) {
        if (inorder[i] !== rootVal) {
            continue;
        }

        let leftInOrder = inorder.slice(0, i);
        let leftPostOrder = postorder.slice(0, i);

        let rightInOrder = inorder.slice(i + 1);
        let rightPostOrder = postorder.slice(i, -1);

        let leftNode = buildTree(leftInOrder, leftPostOrder);

        if (leftNode === null) {
            continue;
        }

        let rightNode = buildTree(rightInOrder, rightPostOrder);

        if (rightNode === null) {
            continue;
        }

        return new TreeNode(rootVal, leftNode, rightNode);
    }

    return null;
};
