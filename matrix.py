class Matrix:
    def __init__(self, content):
        self.content = content

    def __bool__(self):
        for line in self.content:
            if line.count(0) != len(line):
                return False
        return True

    def __add__(self, other):
        # if len(self.content) != len(other.content) or len(self.content[0]) != len(other.content[0]):
        #     return "Matrices must be of the same size!"
        try:
            result = [[0] * len(self.content[0]) for i in range(len(self.content))]
            for i in range(len(self.content)):
                for j in range(len(self.content[0])):
                    result[i][j] = self.content[i][j] + other.content[i][j]
            return result
        except:
            return 'Matrices must be of the same size!'


a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
matrix3 = Matrix([[9, 8, 7, 10], [6, 5, 4, 4], [3, 2, 1, 9]])
matrix4 = Matrix(a)

print(matrix1 + matrix2)
print(matrix2 + matrix4)
print(matrix3 + matrix4)

print(matrix1.__bool__())
print(matrix4.__bool__())
