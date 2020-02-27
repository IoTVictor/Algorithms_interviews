#include <iostream>
using namespace std;

ListNode* lastK_fuc(ListNode* head,int k){
	ListNode* node=head;
	ListNode* cur=head;
	int i=0;
	while(node!=nullptr)
	{
		i++;
		if(i>k) cur=cur->next;
		node=node->next;
	}
	return cur;

};

