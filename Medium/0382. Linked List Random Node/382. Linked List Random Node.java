/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    int n; ListNode head;
    ListNode[] S = new ListNode[101];
    Random random = new Random();

    public Solution(ListNode head) {
        this.head = head;
        ListNode curr = head;

        for (n = 0; curr != null; n++, curr = curr.next) {
            if (n%100 == 0) S[n/100] = curr;
        }
    }

    public int getRandom() {
        int r = random.nextInt(n);
        ListNode curr = S[r/100];
        r %= 100;
        while (r-- > 0) curr = curr.next;
        return curr.val;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */