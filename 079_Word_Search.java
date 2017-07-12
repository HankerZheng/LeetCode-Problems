// Given a 2D board and a word, find if the word exists in the grid.

// The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

// For example,
// Given board =

// [
//   ['A','B','C','E'],
//   ['S','F','C','S'],
//   ['A','D','E','E']
// ]
// word = "ABCCED", -> returns true,
// word = "SEE", -> returns true,
// word = "ABCB", -> returns false.


// Runtime: 17ms

public class Solution {
    
    private int[] dxs = {1, -1, 0, 0};
    private int[] dys = {0, 0, 1, -1};
    
    public boolean exist(char[][] board, String word) {
        if (board.length == 0 || board[0].length == 0) {
            return false;
        }
        if ("".equals(word)) { return true;}
        boolean res = false;
        boolean[][] visited = new boolean[board.length][board[0].length];
        for (int i = 0; i < board.length; i++) {
            for(int j = 0; j < board[0].length; j++) {
                if (board[i][j] == word.charAt(0)) {
                    visited[i][j] = true;
                    res = res || helper(board, word, i, j, 1, visited);
                    visited[i][j] = false;
                }
            }
        }
        return res;
    }
    
    private boolean helper(char[][] board, String word, int x, int y, int pos, boolean[][] visited){
        if (pos == word.length()) {
            return true;
        }
        boolean res = false;
        for(int i = 0; i < dxs.length; i++){
            int nx = x + dxs[i];
            int ny = y + dys[i];
            if (0<=nx && nx<board.length && 0<= ny && ny<board[0].length && !visited[nx][ny]){
                if (board[nx][ny] == word.charAt(pos)){ 
                    visited[nx][ny] = true;
                    res = res || helper(board, word, nx, ny, pos + 1, visited);
                    visited[nx][ny] = false;
                }
            }
        }
        return res;
    }
}