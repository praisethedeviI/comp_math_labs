import numpy as np
from lab2 import SLE



def qr_decomp(A: [[]]):
    A = np.array(A)
    Q = gs(A, row_vecs=False)
    R = np.dot(Q.T, A)
    print(np.dot(Q, R))
    return Q, R

# https://gist.github.com/iizukak/1287876?permalink_comment_id=1348649#gistcomment-1348649
def gs(X: [[]], row_vecs=True, norm=True):
    X = np.array(X)
    if not row_vecs:
        X = X.T
    Y = X[0:1, :].copy()
    for i in range(1, X.shape[0]):
        proj = np.diag(
            (X[i, :].dot(Y.T) / np.linalg.norm(Y, axis=1) ** 2).flat).dot(Y)
        Y = np.vstack((Y, X[i, :] - proj.sum(0)))
    if norm:
        Y = np.diag(1 / np.linalg.norm(Y, axis=1)).dot(Y)
    if row_vecs:
        return Y
    else:
        return Y.T


def solve_QR(Q: [[]], R: [[]], b: []):
    sle = SLE(Q, b)
    sle.solve()
    print(sle.get_vec())
    y = sle.get_vec()
    sle = SLE(R, y)
    sle.reverse()
    x = sle.get_vec()
    return x


def main():
    A = [
        [1, 2, 4],
        [3, 3, 2],
        [4, 1, 3]
    ]
    b = [1, 2, 3]
    Q, R = qr_decomp(A)
    print(Q, R)
    # print(solve_QR(Q, R, b))


if __name__ == '__main__':
    main()
