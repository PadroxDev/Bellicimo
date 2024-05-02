import matplotlib.pyplot as plt

# Placeholder
points = [
    [4, 9.6],
    [8.6, 8],
    [8.2, 4.6],
    [9.4, 5.4],
    [8, 3.2],
    [6, 2],
    [2.5, 2],
    [2, 7],
    [6, 7],
    [4, 9.6]
]

slopes = [
    [3, -0.1],
    [-3, -3.5],
    [2.5, -0.5],
    [0.4, -3],
    [-5, 0],
    [1, -3],
    [-2, 2],
    [2, 1.5],
    [-0.4, 1],
    [3, -0.1]
]

centerPoint = [15, 15]

precision = 50

intervalLength = 30

drawPoints = True
drawSlopes = True
drawCenteredReplica = True
interpolateAbscissas = True
symmetry = True
xSymmetry = True
ySymmetry = True

def PolynomeHermite(x1, x2, x1p, x2p, theta, interpolateAbscissas):
    phi1 = (theta - 1)**2 * (2 * theta + 1)
    phi2 = theta**2 * (-2 * theta + 3)
    phi3 = theta * (theta - 1)**2
    phi4 = theta**2 * (theta - 1)
    if interpolateAbscissas:
        return [phi1 * x1[j] + phi2 * x2[j] + phi3 * x1p[j] + phi4 * x2p[j] for j in range(len(x1))]
    else:
        pointY = phi1 * x1[1] + phi2 * x2[1] + phi3 * (x1p[1]/x1p[0]) * (x2[0] - x1[0]) + phi4 * (x2p[1]/x2p[0]) * (x2[0] - x1[0])
        return pointY

def InterpolationHermite(points, slopes, nbPoints, interpolateAbscissas):
    interpolatedPoints = []
    n = len(points)

    for i in range(n - 1):
        x1, x2 = points[i], points[i + 1]
        x1p, x2p = slopes[i], slopes[i + 1]

        for j in range(nbPoints):
            t = j / precision
            if interpolateAbscissas:
                point = PolynomeHermite(x1, x2, x1p, x2p, t, interpolateAbscissas)
                interpolatedPoints.append(point)
            else:
                point = []
                point.append((j * ((x2[0] - x1[0]) / precision)) + x1[0])
                point.append(PolynomeHermite(x1, x2, x1p, x2p, t, interpolateAbscissas))
                interpolatedPoints.append(point)

    return interpolatedPoints

def DrawPlot(points, slopes, precision, drawPoints, drawSlopes, drawCenteredReplica, center, intervalLength, interpolateAbscissas, symmetry, xSymmetry, ySymmetry):

    # Init
    centerX, centerY = center
    intervalLength = intervalLength * 0.5
    interpolations = InterpolationHermite(points, slopes, precision, interpolateAbscissas)
    fig, ax = plt.subplots()

    # Interpolation
    if len(interpolations) < 2: return (fig, ax)
    ix, iy = zip(*interpolations)
    ax.plot(ix, iy, '-', label='Main Interpolation', color='blue', linewidth=2)

    # Points
    if drawPoints:
        ox, oy = zip(*points)
        ax.plot(ox, oy, 'o', label='Points', color='red')

    # Arrows
    if drawSlopes:
        for (x, y), (dx, dy) in zip(points, slopes):
            ax.arrow(x, y, dx, dy, head_width=0.1, head_length=0.2, fc='green', ec='green', length_includes_head=True)
        ax.plot(0, 0, '-', label='Slopes Arrows', color='green')

    # Centered Replica or Symmetry
    if drawCenteredReplica:
        shiftX = centerX - sum(ix) / len(ix)
        shiftY = centerY - sum(iy) / len(iy)

        ixShifted = [x + shiftX for x in ix]
        iyShifted = [y + shiftY for y in iy]
        ax.plot(ixShifted, iyShifted, '-', label='Centered Interpolation', color='orange', linewidth=2)

    if symmetry:
        ixSym = [2 * centerX - x for x in ix]
        iySym = [2 * centerY - y for y in iy]

        ax.plot(ixSym, iySym, '-', label='Symmetry', color='green', linewidth=2)

    if xSymmetry:
        ixSymX = ix
        iySymX = [2 * centerY - y for y in iy]

        ax.plot(ixSymX, iySymX, '-', label='X-Symmetry', color='Yellow', linewidth=2)

    if ySymmetry:
        ixSymY = [2 * centerX - x for x in ix]
        iySymY = iy

        ax.plot(ixSymY, iySymY, '-', label='Y-Symmetry', color='Cyan', linewidth=2)

    ax.set_xlim(centerX - intervalLength, centerX + intervalLength)
    ax.set_ylim(centerY - intervalLength, centerY + intervalLength)

    # Major Grid
    ax.grid(which='both', linestyle='--', linewidth=0.5, alpha=0.5)
    ax.grid(which='major', linestyle='--', linewidth=0.5, alpha=0.5)

    # Minor Grid
    ax.set_xticks([i for i in range(int(centerX - intervalLength), int(centerX + intervalLength) + 1, 1)])
    ax.set_yticks([i for i in range(int(centerY - intervalLength), int(centerY + intervalLength) + 1, 1)])

    #ax.set_title('Plot Drawer')
    ax.legend()
    return (fig, ax)
