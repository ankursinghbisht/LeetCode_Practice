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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2)
    {
        ListNode* head = new ListNode(-1), * it = head;

        int carry = 0, val;
        while (l1 != NULL && l2 != NULL)
        {
            val = l1->val + l2->val + carry;
            carry = val / 10;
            ListNode* temp = new ListNode(val % 10);
            it->next = temp;
            it = it->next;
            l1 = l1->next;
            l2 = l2->next;
        }

        while (l1 != NULL)
        {
            val = l1->val + carry;
            carry = val / 10;
            it->next = new ListNode(val % 10);
            it = it->next;
            l1 = l1->next;
        }

        while (l2 != NULL)
        {
            val = l2->val + carry;
            carry = val / 10;
            it->next = new ListNode(val % 10);
            it = it->next;
            l2 = l2->next;
        }

        if (carry > 0)
        {
            it->next = new ListNode(carry);
        }

        return head->next;
    }
};