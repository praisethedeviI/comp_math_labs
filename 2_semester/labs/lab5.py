import numpy as np
from lab2 import SLE


def QR(A):
    def step(a):
        v = a / (a[0] + np.copysign(np.linalg.norm(a), a[0]))
        v[0] = 1
        P = np.eye(a.shape[0])
        P -= (2 / np.dot(v, v)) * np.dot(v[:, None], v[None, :])
        return P

    m, n = A.shape
    Q = np.eye(m)
    for i in range(n):
        P = np.eye(m)
        P[i:, i:] = step(A[i:, i])
        Q = np.dot(Q, P)
        A = np.dot(P, A)
    return np.matrix(Q), np.matrix(A)


def solve(A, b):
    Q, R = QR(A)
    Q = Q.tolist()
    sle = SLE(Q, b.tolist())
    sle.solve()
    y = sle.get_vec()
    sle = SLE(R.tolist(), y)
    sle.reverse()
    x = sle.get_vec()
    return x


def main():
    mat = np.array((
        [1, 2, 4],
        [3, 3, 2],
        [4, 1, 3]
    ), dtype=float)

    vec = np.array([4, 2, 3])

    print(solve(mat, vec.copy()))

    sle = SLE(mat.tolist(), vec.tolist())
    print(sle.solve()[1])


if __name__ == '__main__':
    main()
