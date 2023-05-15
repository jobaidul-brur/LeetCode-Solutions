/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) 
    {
        int x, y, a, b;
        int n = 0, i;
        
        for (ListNode *curr = head; curr != nullptr; curr = curr->next, n++);
        x = k; y = n-k+1;
        i=1;
        for (ListNode *curr = head; curr != nullptr; curr = curr->next, i++)
        {
            if (i == x) a = curr->val;
            if (i == y) b = curr->val;
        }
        i=1;
        for (ListNode *curr = head; curr != nullptr; curr = curr->next, i++)
        {
            if (i == x) curr->val = b;
            if (i == y) curr->val = a;
        }
        return head;
    }
};
