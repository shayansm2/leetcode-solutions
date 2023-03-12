// Definition for singly-linked list.
function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val)
    this.next = (next === undefined ? null : next)
}

/**
 * @param {ListNode[]} lists
 * @return {ListNode}
 */
var mergeKLists = function (lists) {
    let len = lists.length;

    if (len === 0) {
        return null;
    }

    let node = undefined;
    let nodeHead = null;

    while (true) {
        let minValue = undefined;
        let minValueIndex = undefined;

        for (let i = 0; i < len; i++) {
            if (lists[i] === undefined || lists[i] == null) {
                continue;
            }

            if (minValue === undefined || minValue > lists[i].val) {
                minValue = lists[i].val;
                minValueIndex = i;
            }
        }

        if (minValue === undefined) {
            break;
        }

        lists[minValueIndex] = lists[minValueIndex].next;

        if (nodeHead === null) {
            nodeHead = new ListNode(minValue);
            node = nodeHead;
        } else {
            node.next = new ListNode(minValue);
            node = node.next;
        }
    }

    return nodeHead;
};
