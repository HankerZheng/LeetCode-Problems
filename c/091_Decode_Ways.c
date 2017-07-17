/*
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.

Subscribe to see which companies asked this question
*/


//for a given message with length i, there are methods[i] ways to decoded the message,
//for every new number given, the last letter decoded could be from either 2-digit number or 1-digit number
//therefore, we have 		methods[i] = methods[i-1](conditionally, when s[i] != '0') + methods[i-2](conditionally, when s[i-1] <= '2' and s[i] <= '6')


//it should be '2' and '6' rather than 2 and 6!!!!!
//we should consider the occasion when there is the digit '0'
//that is, both methods[i-1] and method[i-2] are conditional!!!!

int numDecodings(char* s) {
    int i;
    int *methods;
    int length;
    int result;
    int flag = 0;

    length = strlen(s);		//strlen doesnt include the last '\0'

    if(length == 0)
        return 0;

    methods = (int*)malloc(sizeof(int)*length);
    memset(methods, 0, sizeof(int)*length/ sizeof(char));

//initialize for methods[0]
    if( (s[0]>'0')&&(s[0]<='9') )
    	methods[0] = 1;
    else
    	flag = 1;


//initialize for methods[1]
    if(length != 1)
    {
		if( (s[0]=='2')&&(s[1]<='6') )
		{
			if( s[1] == '0')
		//case: 10 or 20;
				methods[1] = 1;
			else if(s[1] >'0')
		//case: 11, 12, ..., 16, 21, 22, ..., 26;
				methods[1] = methods[0]+1;
			else if(s[1] == 0)
		//wrong input
				flag = 1;
		}
		else if(s[0]=='1')
		{
			if( s[1] == '0')
		//case: 10;
				methods[1] = 1;
			else if( (s[1] >'0')&&(s[1]<='9'))
		//case: 11, 12, ..., 19;
				methods[1] = methods[0]+1;
			else
		//wrong input
				flag = 1;
		}
		else
		{
		    if( (s[1]>'0')&&(s[1]<='9'))
		//case: 01, 02, ..., 09, 17, ..., 19, 27, ..., 29, 30, ..., 99
		        methods[1] = methods[0];
		    else
		//wrong input and 00
    			flag = 1;
		}
	}

//main loop
    for(i = 2; i<length; i++)
    {
    	if( (s[i-1] =='2')&&(s[i]<='6') )
    	{
    		if( s[i] == '0')
    	//case: 20;
    			methods[i] = methods[i-2];
    		else if(s[i] >'0')
    	//case: 21, 22, ..., 26;
    			methods[i] = methods[i-1]+methods[i-2];
    		else
    	//wrong input
    			flag = 1;
    	}    	
    	else if( s[i-1] =='1')
    	{
    		if( s[i] == '0')
    	//case: 10;
    			methods[i] = methods[i-2];
    		else if( (s[i] >'0')&&(s[i]<='9'))
    	//case: 11, 12, ..., 19;
    			methods[i] = methods[i-1]+methods[i-2];
    		else
    	//wrong input
    			flag = 1;
    	}
    	else
    	{
    	    if( (s[i]>'0')&&(s[i]<='9'))
    	//case: 01, 02, ..., 09, 27, ..., 29, 30, ..., 99
    	        methods[i] = methods[i-1];
    	    else
    	//wrong input and 00
    			flag = 1;
    	}
    }

	result = methods[length-1];

	free(methods);

	return flag? 0:result;

}