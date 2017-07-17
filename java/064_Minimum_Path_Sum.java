// Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

// Note: You can only move either down or right at any point in time.

public class Solution {
    public int minPathSum(int[][] grid) {
        if (grid==null || grid[0] == null){
            return 0;
        }
        int[][] minSum = new int[grid.length][grid[0].length];
        int m = grid.length, n = grid[0].length;
        minSum[0][0] = grid[0][0];
        for (int row = 1; row < m; row ++){
            minSum[row][0] = minSum[row-1][0] + grid[row][0];
        }
        for(int col= 1; col < n; col++){
            minSum[0][col] = minSum[0][col-1] + grid[0][col];
        }
        for (int i = 1; i < m; i++){
            for(int j = 1; j < n ; j++){
                minSum[i][j] = Math.min(minSum[i-1][j], minSum[i][j-1]) + grid[i][j];
            }
        }
        return minSum[m-1][n-1];
    }
}