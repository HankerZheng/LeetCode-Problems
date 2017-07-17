/*
Write a function to find the longest common prefix string amongst an array of strings.

Subscribe to see which companies asked this question
*/


//Runtime Error is due to access to the addresss is not available;
//should carefully count the number of n;

char result[10];
char* longestCommonPrefix(char** strs, int strsSize) {

	char thisChar;
	int i,j;
	char* mark = *strs;
	int flag = 0;
	int n;

	if(strsSize == 0)
		return "";
	else if(strsSize == 1)
		return *strs;

	for(j = 0; ;j++)
	{
		mark = *strs + j;
	    thisChar = *mark;
	    if(thisChar == 0)
            break;
	    for(i = 1; i < strsSize; i++)
	    {
	    	if( *(*(strs+i)+j) == 0)
	    	{
	    		flag = 1;
	    		break;
	    	}
	    	else if(thisChar ==  *(*(strs+i)+j) )
	    		;
	    	else
	    	{
	    		flag = 1;
	    		break;
	    	}
	    }
	    if(flag == 1)
	    	break;
	}

    n = mark - (int)*strs ;
    
    if (n == 0)
        return "";
    
	strncpy(result ,*strs, n+1);
	*(result+ n ) = 0;

	return result;
}