// Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

// Example 1:
// Input: [3, 2, 1]

// Output: 1

// Explanation: The third maximum is 1.
// Example 2:
// Input: [1, 2]

// Output: 2

// Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
// Example 3:
// Input: [2, 2, 3, 1]

// Output: 1

// Explanation: Note that the third maximum here means the third maximum distinct number.
// Both numbers with value 2 are both considered as second maximum.

public class Solution {
    public int thirdMax(int[] nums) {
        Integer first = null;
        Integer second = null;
        Integer third = null;
        for (Integer elem: nums){
            if (elem.equals(first) || elem.equals(second) || elem.equals(third)){
                continue;
            }else if(first == null || elem > first){
                third = second;
                second = first;
                first = elem;
            }else if(second == null || elem > second){
                third = second;
                second = elem;
            }else if (third == null || elem > third){
                third = elem;
            }
        }
        return third == null ? first : third;
    }
}