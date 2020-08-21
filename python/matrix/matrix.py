class Matrix:
    def __init__(self, matrix_string):
        self.rows = []
        self.cols = []
        
        row_strs = matrix_string.split('\n')

        for r in row_strs:
            nums = r.strip().split(' ')
            self.rows.append(list(map(int, nums)))

        for x in range(len(self.rows[0])):
            column_nums = []
            for r in self.rows:
                column_nums.append(str(r[x]))

            self.cols.append(list(map(int, column_nums)))


    def row(self, index=None):
        if index:
            return self.rows[index-1]


    def column(self, index=None):
        if index:
            return self.cols[index-1]
