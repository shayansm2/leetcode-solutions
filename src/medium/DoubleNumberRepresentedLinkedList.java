package medium;

import lib.ListNode;

public class DoubleNumberRepresentedLinkedList {
    public ListNode doubleIt(ListNode head) {
        ListNode current = head;
        current.val *= 2;
        if (current.val > 9) {
            current.val -= 10;
            head = new ListNode(1, current);
        }
        while (current != null) {
            ListNode next = current.next;
            if (next != null) {
                next.val *= 2;
                if (next.val > 9) {
                    next.val -= 10;
                    current.val += 1;
                }
            }
            current = current.next;
        }
        return head;
    }
}
