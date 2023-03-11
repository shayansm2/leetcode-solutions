// Definition for singly-linked list.
function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

// Definition for a binary tree node.
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}

/**
 * @param {ListNode} head
 * @return {TreeNode}
 */
var sortedListToBST = function (head) {
    if (head === undefined) {
        return null;
    }

    let array = [];

    while (head) {
        array.push(head.val);
        head = head.next;
    }

    return convertToBST(array);
};

/**
 * @param {Array} array
 * @return {TreeNode}
 */
function convertToBST(array) {
    let len = array.length;

    if (len === 0) {
        return null;
    }

    if (len === 1) {
        return new TreeNode(array.pop());
    }

    let middleIndex = Math.floor(len / 2);

    let leftBST = convertToBST(array.slice(0, middleIndex));
    let rightBST = convertToBST(array.slice(middleIndex + 1, len));

    return new TreeNode(array[middleIndex], leftBST, rightBST);
}