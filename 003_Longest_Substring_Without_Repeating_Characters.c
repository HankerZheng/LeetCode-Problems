/*
Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
*/



int lengthOfLongestSubstring(char* s) {
	int letter[256];
	char* temp = s;
	int count = 0;
	int cur_posi = 0;
	int max_len = 0;
	int i;

	memset(letter, -1, sizeof(int)*256);

	for(; *temp != '\0';)
	{
		if( *(letter+ (int)*temp) == -1)
		{	//this character is present for the first time
			*(letter+ (int)*temp) = cur_posi;
			cur_posi ++;
			count ++;
			temp ++;
			if (count > max_len)
			{
				max_len = count;
			}
		}
		else
		{	// there must be one character conflicting with previous one
			if (count > max_len)
			{
				max_len = count;
			}
			//count from zero, count position starts from the next letter of the conflicting one;
			count = 0;
			cur_posi = *(letter+ (int)*temp)+1;
			temp = s + cur_posi;
			//clear all the flag
			for(i = 0; i<255; i++)
			{
				letter[i] = -1;
			}
		}
	}


	return max_len;

}



/*violent answer which exceeds the time limit*/
int lengthOfLongestSubstring(char* s) {
	char* head;
	char* tail;
	char* temp;
	int max_len = 0;
	int cur_len = 0;
	int flag = 0;


	for(head = s; *head != '\0' ; head++)
	{
		cur_len = 1;
		for(tail= head+1; *tail != '\0'; tail++)
		{
		    flag = 0;
			for(temp = head; temp != tail; temp ++)
			{
				if(*temp ==*tail)
				{
					flag = 1;
					break;
				}
			}
			if(flag == 0)
			{
				cur_len ++;
			}
			else if(cur_len > max_len)
			{
				max_len = cur_len;
				break;
			}
		}
		if(cur_len > max_len)
		{
			max_len = cur_len;
			break;
		}
	}

	return max_len;

}


