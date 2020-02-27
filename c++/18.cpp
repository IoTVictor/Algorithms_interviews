#include <iostream>
using namespace std;

ListNode* delete_fuc(ListNode* head){
	ListNode* pre=head;
	if(head !=nullptr){
	ListNode* p = head->next;
	while(p != nullptr){
		if(p->val != pre->val)
		{
		  pre->next=p;
		  pre=pre->next;
		}
		p=p->next;
		}
	}
        // if end element is duplicated, then the pre->next need to be nullptr
	if(pre!=nullptr)
		pre->next=nullptr;
	return head;
};

