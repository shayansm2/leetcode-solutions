package medium;

import lib.ListNode;

public class RemoveNodesFromLinkedList {
    public ListNode removeNodes(ListNode head) {
        ListNode queue = null;
        while (head != null) {
            while (queue != null && queue.val < head.val) {
                queue = queue.next;
            }
            queue = new ListNode(head.val, queue);
            head = head.next;
        }
        ListNode result = null;
        while (queue != null) {
            result = new ListNode(queue.val, result);
            queue = queue.next;
        }
        return result;
    }
}
