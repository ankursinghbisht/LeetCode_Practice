/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode* head)
    {
        if (!head)
            return false;
        ListNode* t1 = head, * t2 = head->next;
        while (t1 && t2)
        {
            if (t1 == t2)
                return true;
            t1 = t1->next;
            t2 = t2->next;
            if (t2)
                t2 = t2->next;
        }
        return false;
    }
};