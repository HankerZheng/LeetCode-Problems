/*
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {

	struct ListNode *res_temp1, *res_temp2, *head;
	struct ListNode *inp_temp1, *inp_temp2;
	int carry = 0;
	int adder1, adder2;

	inp_temp1 = l1;
	inp_temp2 = l2;
	head = (struct ListNode*)malloc(sizeof(struct ListNode));
	res_temp1 = head;

	for( ; ((inp_temp1 != NULL)||(inp_temp2 != NULL)); )
	{
		res_temp2 = (struct ListNode*)malloc(sizeof(struct ListNode));

		adder1 = inp_temp1 == NULL ? 0: inp_temp1->val;
		adder2 = inp_temp2 == NULL ? 0: inp_temp2->val;

		res_temp2->val = adder1 + adder2 + carry;
		if(res_temp2->val > 9)
		{
			res_temp2->val = (res_temp2->val)%10;
			carry = 1;
		}
		else
		{
			carry = 0;
		}
		res_temp2->next = NULL;

		res_temp1 -> next = res_temp2;

		res_temp1 = res_temp2;
		inp_temp1 = inp_temp1 == NULL ? NULL :inp_temp1->next;
		inp_temp2 = inp_temp2 == NULL ? NULL :inp_temp2->next;
	}

	if (carry)
	{
		res_temp2 = (struct ListNode*)malloc(sizeof(struct ListNode));
		res_temp2->val = carry;
		res_temp2->next = NULL;

		res_temp1 -> next = res_temp2;
	}
	res_temp1 = head->next;
	free(head);

	return res_temp1;

}