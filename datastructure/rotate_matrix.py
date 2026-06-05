class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)

        new = [[0] * n for _ in range(n)]
        # creating a 2d empty matrix with defined boundary
        # for _ in range(n)
        # Runs n times
        # _ means “I don’t care about this variable”

        for i in range(n):
            for j in range(n):
                new[i][j] = matrix[n - j - 1][i]

                # rather than k used maths to get the number

        # copy back to original matrix
        for i in range(n):
            for j in range(n):
                matrix[i][j] = new[i][j]
