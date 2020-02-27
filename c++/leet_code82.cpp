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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* pre_head=new ListNode(-1);
        ListNode* pre=pre_head;
        pre->next=head;
        ListNode* cur=pre->next;
        while(cur !=nullptr)
        {
            ListNode* nex=cur->next;
	   // move nex to the node's val unequal cur->val
            while(nex!=nullptr && nex->val == cur->val)
            {
                    cout<<cur->val<<endl;
                    cur=nex;
                    nex=nex->next;
            }
	    //if cur change means cur is duplicated;
            if(pre->next != cur)
            {
                   pre->next=nex;
            }
            else
            {
                pre=cur;
            }
            cur=pre->next;
        }
        
        if(pre!= nullptr)
            pre->next=nullptr;
        return pre_head->next;   
    }
};
