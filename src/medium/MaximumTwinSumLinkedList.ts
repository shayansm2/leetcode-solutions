class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function pairSum(head: ListNode | null): number {
  let node: ListNode | null = head;
  let lastNodePointer: ListNode | null = head;
  let stack: number[] = [];
  while (lastNodePointer && lastNodePointer.next && node) {
    stack.push(node.val);
    node = node.next;
    lastNodePointer = lastNodePointer.next.next;
  }
  let result: number = 0;
  while (stack && node) {
    result = Math.max(result, stack.pop()! + node.val);
    node = node.next;
  }
  return result;
}
