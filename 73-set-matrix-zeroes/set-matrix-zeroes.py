class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        just use row and col lists to store the indices of the
        zeroth place and then just iterate and get the indices and
        then later on to set rows and columns to zero we need to 
        iterate again and then if either the row or column indice
        is present in the lists , then , we set the ele at
        that place to zero

        """
        row = []
        col = []
        for i in range (len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)
            '''
            get teh location of the "zero " els and then store 
            it in separate lists
            '''
        for i in range(len(matrix)):
            for j in range (len(matrix[i])):
                if i in row or j in col:
                    matrix[i][j] = 0
                    