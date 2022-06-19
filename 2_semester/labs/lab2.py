import time

class SLE:
    def __init__(self, matrix: [[]], vector: []):
        self.m = matrix
        self.v = vector
        self.dim = len(self.v)

    def get_answer(self):
        return self.v

    def solve(self):
        for i in range(self.dim - 1):
            self.__normalize(i)
            for j in range(i + 1, self.dim):
                self.v[j] -= self.v[i]
                for k in range(i, self.dim):
                    self.m[j][k] -= self.m[i][k]

        self.reverse()

        return self.m, self.v

    def reverse(self):

        for i in range(1, self.dim):
            for j in range(i + 1, self.dim + 1):
                self.v[-i] /= self.m[-i][-i]
                self.m[-i][-i] = 1
                factor = self.m[-j][-i]
                self.v[-j] -= self.v[-i] * factor
                for k in range(i, self.dim + 1):
                    self.m[-j][-k] -= self.m[-i][-k] * factor

    def __normalize(self, start):
        for i in range(start, self.dim):
            div = self.m[i][start]
            self.v[i] /= div
            for j in range(self.dim):
                self.m[i][j] /= div

    def get_mat(self):
        return self.m

    def get_vec(self):
        return self.v


def main():
    mat = [
        [10, 3, 3, 1, 2, 1],
        [1, 14, 1, 3, 5, 1],
        [2, 1, 7, 1, 3, 2],
        [1, 2, 2, 12, 3, 1],
        [1, 4, 2, 2, 9, 1],
        [2, 1, 2, 5, 4, 8],
    ]
    vec = [4, 1, 4, 6, 3, 6]
    print(*vec)
    print(*SLE(mat, vec).solve()[1])


if __name__ == '__main__':
    start_time = time.time()
    print(time.time_ns())
    main()
    print("--- %s seconds ---" % round(time.time() - start_time, 10))
