class HashMixin:
    def __hash__(self):
        """the sum of the elements multiplied by their position in the row (the position starts from 1)"""
        ind = [i + 1 for i in range(self.shape[0])]
        return int(sum(sum(x * y for x, y in zip(d, ind)) for d in self.data))


class Matrix(HashMixin):
    def __init__(self, data: list[list], is_hash_matmul=True):
        self.data = data
        self.shape = (0, 0) if len(self.data) == 0 else (len(self.data[0]), len(self.data))
        self.is_hash_matmul = is_hash_matmul
        self.hash_matmul = dict()

    def __add__(self, matrix):
        if self.shape != matrix.shape:
            raise ValueError()

        return Matrix([list(map(sum, zip(*d))) for d in zip(self.data, matrix.data)])

    def __mul__(self, matrix):
        if self.shape != matrix.shape:
            raise ValueError()

        return Matrix([[x * y for x, y in zip(*d)] for d in zip(self.data, matrix.data)])

    def __matmul__(self, matrix):
        def matmul():
            if self.shape[0] != matrix.shape[1]:
                raise ValueError()

            res = [[None] * matrix.shape[0] for _ in range(self.shape[1])]
            for i in range(self.shape[1]):
                for j in range(matrix.shape[0]):
                    res[i][j] = sum(self.data[i][l] * matrix.data[l][j] for l in range(self.shape[0]))
            return Matrix(res)

        if self.is_hash_matmul:
            key = (hash(self), hash(matrix))
            if key not in self.hash_matmul:
                self.hash_matmul[key] = matmul()
            return self.hash_matmul[key]

        return matmul()

    def __str__(self):
        return "\n".join(" ".join(map(str, d)) for d in self.data)
