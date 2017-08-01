// You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

// Write a function to determine if the starting player can guarantee a win.

// For example, given s = "++++", return true. The starting player can guarantee a win by flipping the middle "++" to become "+--+".

// Follow up:
// Derive your algorithm's runtime complexity.


// Time Complexity: O(N) if N is the number of all valid states of the board
// Runtime: 16ms
// Corner Case: state number out of bound if the input string is extremely long.


public class Solution {
    public boolean canWin(String s) {
        long curState = getCurrentState(s);
        HashMap<Long, Boolean> memSearch = new HashMap<>();
        return memSearchCanWin(curState, memSearch);
    }
    
    private long getCurrentState(String s) {
        long res = 0;
        int i = 0;
        long mask = 1;
        while (i < s.length()){
            while (i < s.length() && s.charAt(i) == '+'){
                res += mask;
                mask = mask << 1;
                i++;
            }
            mask = mask << 1;
            while (i < s.length() && s.charAt(i) == '-'){ i++;}
        }
        return res;
    }
    
    private boolean memSearchCanWin(long curState, HashMap<Long, Boolean> memSearch) {
        if (memSearch.containsKey(curState)){
            return memSearch.get(curState);
        }
        boolean oppoRes = true;
        long mask = 0b11;
        while (mask <= curState) {
            if ((mask & curState) == mask ){
                oppoRes = oppoRes && memSearchCanWin(curState - mask, memSearch);
            }
            mask = mask << 1;
        }
        memSearch.put(curState, !oppoRes);
        return !oppoRes;
    }
}