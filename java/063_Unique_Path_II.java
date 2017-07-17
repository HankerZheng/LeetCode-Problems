// Follow up for "Unique Paths":

// Now consider if some obstacles are added to the grids. How many unique paths would there be?

// An obstacle and empty space is marked as 1 and 0 respectively in the grid.

// For example,
// There is one obstacle in the middle of a 3x3 grid as illustrated below.

// [
//   [0,0,0],
//   [0,1,0],
//   [0,0,0]
// ]
// The total number of unique paths is 2.

// Note: m and n will be at most 100.
public class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        if(obstacleGrid == null || obstacleGrid[0] == null){
            return 0;
        }
        int rowCnt = obstacleGrid.length, colCnt = obstacleGrid[0].length;
        int index = 0;
        while (index < rowCnt && obstacleGrid[index][0] != 1){
            obstacleGrid[index++][0] = -1;
        }
        index = 0;
        while (index < colCnt && obstacleGrid[0][index] != 1){
            obstacleGrid[0][index++] = -1;
        }
        for(int i = 1; i < rowCnt; i ++){
            for(int j = 1; j < colCnt; j++){
                if (obstacleGrid[i][j] == 0){
                    obstacleGrid[i][j] = - (getMethod(obstacleGrid, i-1, j) + getMethod(obstacleGrid, i, j-1));
                }
            }
        }
        return getMethod(obstacleGrid, rowCnt-1, colCnt-1) ;
    }
    public int getMethod(int[][] obstacleGrid, int i ,int j){
        return obstacleGrid[i][j]==1? 0: -obstacleGrid[i][j];
    }
}