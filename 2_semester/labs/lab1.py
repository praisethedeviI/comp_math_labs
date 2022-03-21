import math
from numpy import linalg, matmul

b = [1 for i in range(10)]
a = [
    [1, 0, -1],
    [0, 1, 0],
    [1, 0, 1]
]


def mat_gilbert(dim):  # a_ij = 1/(i+j-1)
    m = []
    for i in range(dim):
        m.append([])
        for j in range(dim):
            m[i].append(1 / (i + j + 1))
    return m


def mat_lemer(dim):  # a_ij = min(i,j)/max(i,j)
    m = []
    for i in range(dim):
        m.append([])
        for j in range(dim):
            m[i].append(min(i + 1, j + 1) / max(i + 1, j + 1))
    return m


def mat_custom(dim, const):  # C + log_2(i*j)
    m = []
    for i in range(dim):
        m.append([])
        for j in range(dim):
            m[i].append(const + math.log((i + 1) * (j + 1), 2))
    return m


def main():
    m_g = mat_gilbert(10)
    m_l = mat_lemer(10)
    m_c = mat_custom(10, 500)
    m_g_cond = linalg.cond(m_g)
    m_l_cond = linalg.cond(m_l)
    m_c_cond = linalg.cond(m_c)
    print(m_g_cond, m_l_cond, m_c_cond)

    x = linalg.solve(m_g, b)
    print("Матрица иксов", x)
    c = matmul(m_g, x)
    print(c)
    diff = [abs(b[i] - c[i]) for i in range(len(c))]
    print("Матрица разницы", diff)


if __name__ == '__main__':
    main()
