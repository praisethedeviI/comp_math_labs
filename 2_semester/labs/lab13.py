import numpy as np


def get_max(A):
    index = (1, 0)
    for i in range(A.shape[0]):
        for j in range(i):
            if abs(A[index]) < abs(A[i, j]):
                index = (i, j)
    return index


def rotation_method(A):

    for k in range(15):
        l, m = get_max(A)
        phi = np.arctan(2 * A[l, m] / (A[l, l] - A[m, m])) / 2
        T = np.eye(A.shape[0])
        T[l, l] = np.cos(phi)
        T[l, m] = -np.sin(phi)
        T[m, l] = np.sin(phi)
        T[m, m] = np.cos(phi)

        A = T.T * A * T

    return A


def main():
    vec = np.matrix([
        [-0.168700, 0.353699, 0.008540, 0.733624],
        [0.353699, 0.056519, 0.723182, -0.076440],
        [0.008540, 0.723182, 0.015938, 0.342333],
        [0.733624, -0.076440, 0.342333, -0.045744]
    ])
    np.set_printoptions(precision=4, suppress=True)

    print(rotation_method(vec).diagonal())


if __name__ == '__main__':
    main()

