// A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

// For example, given three people living at (0,0), (0,4), and (2,2):

// 1 - 0 - 0 - 0 - 1
// |   |   |   |   |
// 0 - 0 - 0 - 0 - 0
// |   |   |   |   |
// 0 - 0 - 1 - 0 - 0
// The point (0,2) is an ideal meeting point, as the total travel distance of 2+2+2=6 is minimal. So return 6.

// Space: O(K), where k is the number of persons in the grid, at worst case, k = m*n
// Time: O(m*n)

public class Solution {
    public int minTotalDistance(int[][] grid) {
        
        int m = grid.length;
        int n = grid[0].length;
        
        List <Integer> xcoor = new ArrayList();
        List <Integer> ycoor = new ArrayList();
        for (int i=0; i<m; i++){
            for (int j=0; j<n; j++){
                if (grid[i][j] == 1){
                    xcoor.add(i);
                    ycoor.add(j);
                }
            }
        }
        
        Collections.sort(xcoor);
        Collections.sort(ycoor);
        int start = 0;
        int end = xcoor.size() - 1;
        int ans = 0;
        while (start < end){
            ans += xcoor.get(end) - xcoor.get(start);
            ans += ycoor.get(end) - ycoor.get(start);
            start += 1;
            end -= 1;
        }
        return ans;
        
        
    }
}