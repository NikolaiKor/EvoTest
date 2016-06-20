import random


class Test1:
    def __init__(self):
        self.n = 10
        self.max_coordinate = [[0, 0], [0, 0], [0, 0]]  # current coordinate of max columns
        self.max = [0, 0, 0]  # current max columns length
        self.columns = [[], [], []]  # current max columns
        self.columns_match = [['i', 'j'], ['i', 'k'], ['j', 'k']]  # dimension result matching

    # Generate matrix n*n*n
    def generate(self):
        matrix1 = []
        for i in range(self.n):
            matrix2 = []
            for j in range(self.n):
                matrix3 = []
                for k in range(self.n):
                    matrix3.append(random.randint(0, 10))
                matrix2.append(matrix3)
            matrix1.append(matrix2)
        return matrix1

    # Find 3 max columns in matrix
    def analyse(self, arr):
        for i in range(self.n):
            for j in range(self.n):
                count = [0, 0, 0]  # 3d counter (i, j, k)
                columns = [[], [], []]  # temporary maximum columns
                for k in range(self.n):
                    count[0] += arr[i][j][k]  # (i;j) counter
                    count[1] += arr[i][k][j]  # (i;k) counter
                    count[2] += arr[k][i][j]  # (j;k) counter
                    columns[0].append(arr[i][j][k])
                    columns[1].append(arr[i][k][j])
                    columns[2].append(arr[k][i][j])
                for l in range(3):
                    self.check(count[l], columns[l], l, i, j)
        # Answer generating. answer with column coordinates, column length and column members
        res = []
        for i in range(3):
            res.append(((self.columns_match[i][0], self.max_coordinate[i][0]),
                        (self.columns_match[i][1], self.max_coordinate[i][1]),
                        self.max[i], self.columns[i]))
        return res

    # Check is column max
    def check(self, count, column, i, x, y):
        if count > self.max[i]:
            self.max[i] = count
            self.max_coordinate[i] = [x, y]
            self.columns[i] = column


# Test
a = Test1()
b = a.generate()
res = a.analyse(b)

for i in range(a.n):
    print(b[i])
print()
for i in range(3):
    print(res[i])
