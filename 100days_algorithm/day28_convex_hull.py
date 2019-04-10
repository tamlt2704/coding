import numpy as np

def split(u, v, points):
    # return points on left side of UV
    return [p for p in points if np.cross(p-u, v-u) < 0]


def extend(u, v, points):
    if not points:
        return []

    # find furthest point W, and split search to WV, UV
    w = min(points, key=lambda p: np.cross(p-u, v-u))
    p1, p2 = split(w, v, points), split(u, w, points)
    return extend(w, v, p1) + [w] + extend(u, w, p2)

def convex_hull(points):
    # find two hull points, U, V and split to left and right search
    u = min(points, key=lambda p: p[0])
    v = max(points, key=lambda p: p[0])

    left, right = split(u, v, points), split(v, u, points)
    return [v] + extend(u, v, left) + \
            [u] + extend(v, u, right) + [v]

points = np.random.rand(100, 2)
print(np.array(convex_hull(points)))


