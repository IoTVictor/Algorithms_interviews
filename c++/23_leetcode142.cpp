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
    ListNode *detectCycle(ListNode *head) {
        ListNode* fast=head;
        ListNode* low= head;
        while(1){
            if(fast== nullptr) {return nullptr;}
            fast=fast->next;
            low=low->next;
            if(fast== nullptr) {return nullptr;}
            fast=fast->next;
            if(fast==low) break;
        }
        cout<<1<<endl;
        fast=head;
        while(fast!=low)
        {
            fast=fast->next;
            low=low->next;
        }
        return low;
    }
};
