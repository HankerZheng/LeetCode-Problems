// A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

// For example, given three people living at (0,0), (0,4), and (2,2):

// 1 - 0 - 0 - 0 - 1
// |   |   |   |   |
// 0 - 0 - 0 - 0 - 0
// |   |   |   |   |
// 0 - 0 - 1 - 0 - 0
// The point (0,2) is an ideal meeting point, as the total travel distance of 2+2+2=6 is minimal. So return 6.

// Time: O(m*n) 
// Space: O(n + m)

public class Solution {
    public int minTotalDistance(int[][] grid) {
        if(grid==null || grid[0] == null) return 0;
        int m = grid.length, n = grid[0].length;
        int[] personRow = new int[m];
        int[] personCol = new int[n];
        for (int row = 0; row < m; row ++){
            for(int col = 0; col < n; col++){
                if (grid[row][col] == 1){
                    personRow[row] += 1;
                    personCol[col] += 1;
                }
            }
        }
        return getDistance(personRow) + getDistance(personCol);
    }
    
    public int getDistance(int[] person){
        int left = 0, right = person.length - 1;
        int dist = 0;
        while (left < right){
            while (left < right && person[left] == 0){
                left ++;
            }
            while(left < right && person[right] == 0){
                right --;
            }
            int minCnt = Math.min(person[left], person[right]);
            dist += (right - left) * minCnt;
            person[left] -= minCnt;
            person[right] -= minCnt;
        }
        return dist;
    }
}