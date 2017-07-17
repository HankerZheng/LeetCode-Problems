// Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

// You have the following 3 operations permitted on a word:

// a) Insert a character
// b) Delete a character
// c) Replace a character

public class Solution {
    public int minDistance(String word1, String word2) {
        int length1 = word1.length();
        int length2 = word2.length();
        int[][] minDist = new int[length1 + 1][length2 + 1];
        
        for(int i = 0; i <= length1; i++){
            minDist[i][0] = i;
        }
        for(int j = 0; j <= length2; j++){
            minDist[0][j] = j;
        }
        for(int i = 1; i <= length1; i++){
            for(int j = 1; j <= length2; j++){
                int deleteDist = 1 + minDist[i][j-1];
                int insertDist = 1 + minDist[i-1][j];
                int replaceDist = (word1.charAt(i-1)==word2.charAt(j-1)?0:1) + minDist[i-1][j-1];
                minDist[i][j] = Math.min(deleteDist, Math.min(insertDist, replaceDist));
            }
        }
        return minDist[length1][length2];
    }
}