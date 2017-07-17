/*
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

Subscribe to see which companies asked this question
*/
char* longestPalindrome(char* s) {

    int A[1000][1000] = {0};	//A[i][j] represents whether s[i..j] is palindormix substring
    int i,j;
    int num;
    int maxline = 1;
    int flag;
    char* answer;
    char* mark = 0;


    //initialization
    for(j = 0; *(s+j) != 0; j++)
    {
    	A[j][j] = 1;
    	if(mark == 0)
            mark = s+j;
    	if ((*(s+j+1) != '\0')&&( *(s+j+1) ==  *(s+j) ))
    	{
    		A[j][j+1] = 1;
    		maxline = 2;
    		mark = s+j;
    	}
    }
    num = j;	//*(s+num) == '\0'

    if(j == 1)
    	return s;
    if(j == 2)
    {
        if(maxline == 2)
            return s;
        else
            return s+1;
    }

    for(j = 2; j < num; j++ )
    {
    	for(i = 0; i+j <num; i++)
    	{
    		flag = (A[i+1][i+j-1])&&(*(s+i) == *(s+i+j));
    		if (flag)
    		{
    			A[i][i+j] = 1;
    			maxline = j+1;
    			mark = s+i;
    		}
    		else
    			A[i][i+j] = 0;
    	}
    }

    answer = (char*) malloc(sizeof(char)*(maxline+1));
    strncpy(answer,mark,maxline);
    *(answer+maxline) = 0;
    return answer;
}
