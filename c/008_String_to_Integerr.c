/*
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.

spoilers alert... click to show requirements for atoi.

Subscribe to see which companies asked this question
*/


// understanding different between ~ and !, the former is bit wise NOT and the latter is logical negation

#define int32MAX 2147483647
#define int32MIN -2147483648

bool is_beyond_boundary(bool flag, int num, int digit)
{
	int num_temp = num;

	if(flag)	//negetive number boundary
	{
		num = - num;
		if (num > int32MIN/10 )
			return 0;
		else if(num == int32MIN/10)
		{	
			if( digit <= 8)
				return 0;
			else 
				return 1;
		}
		else
			return 1;
	}
	else
	{
		if (num < int32MAX / 10)
			return 0;
		else if(num == int32MAX /10)
		{
			if(digit <= 7)
				return 0;
			else
				return 1;
		}
		else
			return 1;
	}
}


int myAtoi(char* str) {
    
    char* str_in = str;
    bool flag_others;
    bool flag_sign;	//1 reprensents negetive
    int result = 0;

    //ignore spaces only
    while(*str_in == ' ')
    {
    	str_in++;
    	if(*str_in == 0)
    		return 0;
    }

    flag_others =  !((*str_in <= '9')&&(*str_in >= '0')||(*str_in == '-')||(*str_in == '+'));
    
    if(flag_others)
        return 0;
    else if(*str_in == '-')
    {
    	flag_sign = 1;    
    	str_in++;
        if(*str_in == 0)
	    	return 0;
    }
    else if(*str_in == '+')
    {
    	flag_sign = 0;    
    	str_in++;
        if(*str_in == 0)
	    	return 0;
    }
    else
        flag_sign = 0;
    
    flag_others =  !((*str_in <= '9')&&(*str_in >= '0'));    // new flag without checking '-' and '+'
    
    while(!flag_others)
    {
    	if( is_beyond_boundary(flag_sign, result, *str_in-'0') )
    		return flag_sign? int32MIN:int32MAX;

    	result = result *10 + *str_in - '0';
    	str_in++;
    	flag_others =  !((*str_in <= '9')&&(*str_in >= '0'));
    }

    return (flag_sign)? -result : result;
    
}