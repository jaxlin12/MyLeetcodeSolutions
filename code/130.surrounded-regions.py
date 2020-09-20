#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        row = len(board)
        if row == 0:
            return
        col = len(board[0])
        if col == 0:
            return
        queue = collections.deque()
        for j in range(col):
            if board[0][j] == 'O':
                queue.append((0, j))
            if col > 1:
                if board[-1][j] == 'O':
                    queue.append((row-1, j))
        for i in range(1, row):
            if board[i][0] == 'O':
                queue.append((i, 0))
            if row > 1:
                if board[i][-1] == 'O':
                    queue.append((i, col-1))

        while len(queue) != 0:
            i, j = queue.popleft()
            board[i][j] = 'P'
            if i - 1 >= 0:
                if board[i-1][j] == 'O':
                    queue.append((i-1, j))
            if i + 1 < row:
                if board[i+1][j] == 'O':
                    queue.append((i+1, j))
            if j - 1 >= 0:
                if board[i][j-1] == 'O':
                    queue.append((i, j-1))
            if j + 1 < col:
                if board[i][j+1] == 'O':
                    queue.append((i, j+1))

        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = 'X'
                elif board[i][j] == 'P':
                    board[i][j] = 'O'
        
        
# @lc code=end

