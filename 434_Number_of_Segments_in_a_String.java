// Count the number of segments in a string, where a segment is defined to be a contiguous sequence of non-space characters.

// Please note that the string does not contain any non-printable characters.

// Example:

// Input: "Hello, my name is John"
// Output: 5

public class Solution {
    public int countSegments(String s) {
        int count = 0;
        boolean prevSpace = true, currentSpace = true;
        for(int idx = 0; idx < s.length(); idx++){
            currentSpace = s.charAt(idx) == ' ';
            if (currentSpace && !prevSpace){
                count ++;
            }
            prevSpace = currentSpace;
        }
        if (!currentSpace){
            count ++;
        }
        return count;
        
    }
}