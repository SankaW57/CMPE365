from numpy import random, sqrt, log, sin, cos, pi
import numpy as np
from math import atan2
from random import randint
from scipy.stats import norm
from matplotlib import pyplot as plt

yA_plane = None
xA_plane = None
yB_plane = None
xB_plane = None

# Points for sets A and B
xA, yA, xB, yB = ([] for i in range(4))


# transformation function
def gaussian(w1, w2):
    xz1 = sqrt(-2 * log(w1)) * cos(2 * pi * w2)
    xz2 = sqrt(-2 * log(w1)) * cos(2 * pi * w2)
    z1 = sqrt(-2 * log(w1)) * cos(2 * pi * w2)
    z2 = sqrt(-2 * log(w1)) * sin(2 * pi * w2)
    return z1, z2


def plotIt(coords, convex_hull=None):
    xs, ys = zip(*coords)
    plt.scatter(xs, ys)

    if convex_hull != None:

        for i in range(1, len(convex_hull) + 1):

            if i == len(convex_hull): i = 0  # wrap
            c0 = convex_hull[i - 1]
            c1 = convex_hull[i]
            plt.plot((c0[0], c1[0]), (c0[1], c1[1]), 'r')
    plt.show()


def createPoints(ct, min=-100, max=100):
    return [[randint(min, max), randint(min, max)] \
            for _ in range(ct)]


def det(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) \
           - (p2[1] - p1[1]) * (p3[0] - p1[0])


def createGaussPoints(ct, min=-100, max=100):
    return [[np.random.normal(min, max), np.random.normal(min, max)] \
            for _ in range(ct)]


def distance(p0, p1=None):
    if p1 == None: p1 = anchor
    y_span = p0[1] - p1[1]
    x_span = p0[0] - p1[0]
    return y_span ** 2 + x_span ** 2


def quicksort(a):
    if len(a) <= 1: return a
    smaller, equal, larger = [], [], []
    piv_ang = polar_angle(a[randint(0, len(a) - 1)])

    for pt in a:
        pt_ang = polar_angle(pt)

        if pt_ang < piv_ang:
            smaller.append(pt)

        elif pt_ang == piv_ang:
            equal.append(pt)

        else:
            larger.append(pt)

    return quicksort(smaller) \
           + sorted(equal, key=distance) \
           + quicksort(larger)


def scatter_plot(coords, convex_hull=None):
    xs, ys = zip(*coords)
    plt.scatter(xs, ys)

    if convex_hull != None:
        for i in range(1, len(convex_hull) + 1):
            if i == len(convex_hull): i = 0  # wrap
            c0 = convex_hull[i - 1]
            c1 = convex_hull[i]
            plt.plot((c0[0], c1[0]), (c0[1], c1[1]), 'r')
    plt.show()


def grahamScan(points, show_progress=False):
    global anchor

    min_idx = None
    for i, (x, y) in enumerate(points):
        if min_idx == None or y < points[min_idx][1]:
            min_idx = i
        if y == points[min_idx][1] and x < points[min_idx][0]:
            min_idx = i

    anchor = points[min_idx]

    sorted_pts = quicksort(points)
    del sorted_pts[sorted_pts.index(anchor)]
    hull = [anchor, sorted_pts[0]]

    for s in sorted_pts[1:]:
        while det(hull[-2], hull[-1], s) <= 0:
            del hull[-1]
        hull.append(s)
        if show_progress: scatter_plot(points, hull)
    return hull

def polar_angle(p0, p1=None):
    if p1 == None: p1 = anchor
    y_span = p0[1] - p1[1]
    x_span = p0[0] - p1[0]
    return atan2(y_span, x_span)


setA = createGaussPoints(1000)
setB = createPoints(100)
print ("Printing Lists")
print ("This is list A: ", list(setA))
print("This is list B: ", setB)
hull = grahamScan(list(setA), False)
scatter_plot(setA, hull)