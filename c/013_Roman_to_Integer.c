/*
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

Subscribe to see which companies asked this question
*/

// if thisNum < nextNum, then plus -thisNum

int romanToInt(char* s) {
    int table[90];  //cuz 'Z' = 90 and Z is not a Rome number
    int thisNum;
    int nextNum;
    int result = 0;
    char*ptr = s;
    
    //initialize table
    table[0] = 0;
    table['I'] = 1;
    table['V'] = 5;
    table['X'] = 10;
    table['L'] = 50;
    table['C'] = 100;
    table['D'] = 500;
    table['M'] = 1000;
    
    while(*ptr!= 0)
    {
        thisNum = table[*ptr];
        nextNum = table[*(ptr+1)];
        if(thisNum < nextNum)
            result += -thisNum;
        else
            result += thisNum;
        ptr++;
    }
    return result;
}