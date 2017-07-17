/*
Given an integer, convert it to a roman numeral.

Input is guaranteed to be within the range from 1 to 3999.

Subscribe to see which companies asked this question
*/


//in the outest for loop, i could be equal to 0!!!

char* intToRoman(int num) {
    
    char* result;
    char* ptr;
    int i;
    int j, MyPow_ten = 1;
    int digit;
    char rome[8] = {'I', 'V', 'X', 'L', 'C', 'D', 'M', 'N'};


    result = (char*) malloc( sizeof(char)*20);
    ptr = result;

    for(i = 3; i >= 0; i --)
    {
    	for (j = 0, MyPow_ten = 1; j<i; j++)
			MyPow_ten *=10;

    	digit = num / MyPow_ten %10;
		if(digit == 0)
			;
		else if(digit < 4)
		{
			for( j = digit; j>0; j--)
			{
				*ptr = rome[2*i];
				ptr++;
			}
		}
		else if(digit == 4)
		{
			*ptr = rome[2*i];
			ptr++;
			*ptr = rome[2*i+1];
			ptr++;
		}
		else if(digit < 9)
		{
			*ptr = rome[2*i+1];
			ptr++;
			for( j = digit - 5; j > 0; j--)
			{
				*ptr = rome[2*i];
				ptr++;
			}
		}
		else	//digit == 9
		{
			*ptr = rome[2*i];
			ptr++;
			*ptr = rome[2*i+2];
			ptr++;
		}
	}
	*ptr = 0;

	return result;
}