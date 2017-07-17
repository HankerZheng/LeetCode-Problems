# Given a 2D board containing 'X' and 'O' (the letter O),
# capture all regions surrounded by 'X'.

# A region is captured by flipping all 'O's into 'X's in that surrounded region.

# For example,
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:

# X X X X
# X X X X
# X X X X
# X O X X
# Subscribe to see which companies asked this question


# Runtime: 156 ms
class Solution(object):
    def solve(self, board):
        def mark_neighbor(position):
            this_x, this_y = position
            for dx, dy in delta:
                x,y = this_x+dx, this_y+dy
                if 0<=x<max_x and 0<=y<max_y and (x*max_x+y) not in visited and board[x][y] == 'O':
                    visited.add(x*max_x+y)
                    queue.append((x,y))

        if not board or not board[0]:
            return
        visited = set([])
        max_x, max_y = len(board), len(board[0])
        delta = [(0,1),(1,0),(-1,0),(0,-1)]
        queue = []
        # first, scan the border, store all the 'O'
        # into the queue
        for i,_ in enumerate(board):
            if board[i][0] == 'O':
                visited.add(i*max_x+0)
                queue.append((i,0))
            if board[i][max_y-1] == 'O':
                visited.add(i*max_x+max_y-1)
                queue.append((i, max_y-1))
        for j,_ in enumerate(board[0]):
            if board[0][j]=='O' and j not in visited:
                visited.add(j)
                queue.append((0,j))
            if board[max_x-1][j]=='O' and ((max_x-1)*max_x+j) not in visited:
                visited.add((max_x-1)*max_x+j)
                queue.append((max_x-1, j))
        # mark all the 'O' that is the neighbor of the point in the queue
        while queue:
            this_point = queue.pop(0)
            mark_neighbor(this_point)
        for i,row in enumerate(board):
            for j, value in enumerate(row):
                if board[i][j]=='O' and (i*max_x+j) not in visited:
                    board[i][j] = 'X'





    def solve_DFS_TLE(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        def dfs(x,y):
            count = 0
            visited[x][y] = -1
            for dx, dy in delta:
                new_x, new_y = x+dx, y+dy
                if 0<=new_x<=max_x and 0<=new_y<=max_y:
                    if board[new_x][new_y] == 'X':
                        count += 1
                    elif board[new_x][new_y] == 'O':
                        if visited[new_x][new_y]==0:
                            dfs(new_x, new_y)
                            count += (1 if board[new_x][new_y]=='X' else 0)
                        elif visited[new_x][new_y]==-1:
                            # add 1 when the state is pending
                            count += 1
            if count == 4:
                board[x][y] = 'X'
            else:
                visited[x][y] = 1


        if not board or not board[0]:
            return
        # init
        # visited: 0(unvisited), -1(pending), 1(visited)
        max_x, max_y = len(board)-1, len(board[0])-1
        delta = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = [[0 for _ in row] for row in board]
        # traverse the board
        for i,row in enumerate(board):
            for j,value in enumerate(row):
                if value == 'O' and visited[i][j] == 0:
                    # in the dfs, search all not visited 'O'
                    # mark them as 'X' if is surrounded
                    dfs(i,j)

if __name__ == '__main__':
    sol = Solution()
    matrix = [['O','X','O'],['X','O','X'],['O','X','O']]
    sol.solve_DFS_TLE(matrix)
    print matrix
