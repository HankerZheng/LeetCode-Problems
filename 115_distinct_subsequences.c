/*
Given a string S and a string T, count the number of distinct subsequences of T in S.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.

Subscribe to see which companies asked this question
*/

//

struct fit_subseq
{
	int index_in_subseq;
	int count_flag;
};


int numDistinct(char* s, char* t) {

    int i,j;
    int len_s = strlen(s);
    int len_t = strlen(t);
    int** dp;
    char* ptr_s = s;
    char* ptr_t = t;

    int result;

    if( (len_s == 0)||(len_t == 0) )
    	return 0;

    //subsequence check
    for(ptr_s = s; *ptr_s != 0; ptr_s++)
    {
    	if(*ptr_t == 0)
    		break;
    	else if(*ptr_t == *ptr_s)
    		ptr_t ++;
    }
    if(*ptr_t != 0)	//is_not_subsequense
    	return 0;

    //allocate space for matrix of dp
    dp = (int**) malloc(sizeof(int*)*len_s);
    dp[0] = (int*) malloc(sizeof(int)*len_s*len_t);
    memset(dp[0], 0, sizeof(int)*len_s*len_t/sizeof(char));
    for(i = 1; i < len_s; i++)
    {
    	dp[i] = dp[i-1]+len_t;
    }

    //matrix initialize
    if(s[0] == t[0])
    	dp[0][0] = 1;
    else
    	dp[0][0] = 0;

    for(i = 1; i < len_s; i++)
    {
    	dp[i][0] = (s[i] == t[0]) ? (dp[i-1][0]+1) : (dp[i-1][0]);
    }

    //dp starts
    for(j = 1; j < len_t; j ++)
    {
    	for(i = j; i < len_s; i++)
    	{
    		if( s[i] == t[j])
    			dp[i][j] = dp[i-1][j-1] + dp[i-1][j];	//with last + without last
    		else
    			dp[i][j] = dp[i-1][j];
    	}

    }

    result = dp[len_s-1][len_t-1];

    free(dp[0]);
    free(dp);

    return result;

}
