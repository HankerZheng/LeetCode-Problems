public class Solution {
    int[][] delta = {{0,1}, {1,0}, {-1,0}, {0,-1}};
    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0){return 0;}
        int rows = grid.length;
        int cols = grid[0].length;
        int islandCnt = 0;
        boolean[][] visited = new boolean[rows][cols];
        
        for (int i = 0; i < rows; i ++){
            for (int j = 0; j < cols; j++){
                if (visited[i][j] == false && grid[i][j] == '1'){
                    visitAllLand(grid, i, j, visited);
                    islandCnt ++;
                }
            }
        }
        return islandCnt;
    }
    
    public void visitAllLand(char[][] grid, int i, int j, boolean[][] visited){
        for(int[] deltaij: delta){
            int ni = i + deltaij[0];
            int nj = j + deltaij[1];
            if (validPos(ni, nj, grid) && grid[ni][nj] == '1' && visited[ni][nj] == false){
                visited[ni][nj] = true;
                visitAllLand(grid, ni, nj, visited);
            }
        }
    }
    
    public boolean validPos(int i, int j, char[][]grid){
        return 0<=i && i<grid.length && 0<=j && j<grid[0].length;
    }
}