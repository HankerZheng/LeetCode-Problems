
/*
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
Subscribe to see which companies asked this question

*/

//free 了不该 free的地址 因此这道题目花了好多时间
//when we free head+1, cuz we allocated from head to head+3, all the head behind would be freed;

struct letter_link
{
	char letter;
	struct letter_link *next;
};


int increment_i(int p, int numRows)
{
	int flag = p%(2*numRows - 2);

	if (numRows == 1 )
        return 0;
	if(flag < numRows)
		return flag;
	else
	{
		return 2*numRows - 2 - flag;
	}
}


char* convert(char* s, int numRows) {
    int i,p;
    struct letter_link *head;
    struct letter_link *line_temp;
    struct letter_link *link_temp;
    struct letter_link *free_temp;
    char *char_temp;
    char *answer;

    if(numRows == 1)
        return s;

    head = (struct letter_link*) malloc(sizeof(struct letter_link)*numRows);
    memset(head, 0, sizeof(struct letter_link)*numRows);

    for(char_temp=s, p = 0; *char_temp!=0; char_temp++, p++)
    {
		i = increment_i(p, numRows);

    	for(line_temp = (head+i); line_temp->next != NULL; line_temp = line_temp->next)
			;
	    if(line_temp->letter == 0)
		{
			line_temp->letter = *char_temp;
		}
		else
		{
			link_temp = malloc(sizeof(struct letter_link));
			link_temp->letter = *char_temp;
			link_temp->next = NULL;
			line_temp->next = link_temp;
		}
    }

    answer = (char*) malloc(sizeof(char)*(strlen(s)+1) );
    for(i = 0, p = 0; i < numRows; i++)
    {
    	for(line_temp = head+i; line_temp != NULL;)
    	{
    		*(answer+p) = line_temp->letter;
    		p++;
    		free_temp = line_temp;
    		line_temp = line_temp->next;
    		if ((free_temp>= head)&&(free_temp < (head+numRows)))
    		    ;
    		else
    		    free(free_temp);
    		
    	}
    }

    *(answer+p) = 0;


    return answer;
}
