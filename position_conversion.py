import numpy as np


def transform_coordinates(pos):
    # takes a np.array of (n,3) as xyz
    pos2 = np.zeros_like(pos)
    for i in range(3):
        pos2[:, i] = pos[:, i] - pos[0, i]
    v01 = pos2[1, :]
    v_i = v01 / np.linalg.norm(v01)

    for i in range(2, pos2.shape[0]):
        v02 = pos2[i, :]
        uv02 = v02 / np.linalg.norm(v02)
        cos_12 = np.dot(v_i, uv02)
        if 1 - np.abs(cos_12) > 1e-6:
            break
        if i == pos2.shape[0]:
            raise Exception("The given coordinates are in one line.")
    if np.abs(cos_12) < 1e-6:
        v_j = uv02
    else:
        v_j = uv02 / cos_12 - v_i
        v_j = v_j / np.linalg.norm(v_j)

    v_k = np.cross(v_i, v_j)
    r = np.zeros((3, 3))
    r[:, 0] = v_i
    r[:, 1] = v_j
    r[:, 2] = v_k

    pos2 = np.dot(np.linalg.pinv(r), pos2.T).T
    pos2[np.abs(pos2) < 1e-6] = 0
    return pos2


if __name__ == "__main__":
    from scipy.spatial import distance_matrix

    m = np.random.random((4, 3))
    print(distance_matrix(m, m))
    m_norm = transform_coordinates(m)
    print(distance_matrix(m_norm, m_norm))
