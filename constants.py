from point import Point

CURRENT_VERSION = "0.1.1"
DEFAULT_WIDTH = 1920
DEFAULT_HEIGHT = 1080
DEFAULT_TITLE = "Projet Mathématiques G.Tech 2"
ADD_POINT_WINDOW = "Add New Point"
ADD_POINT_WIDTH = 500
ADD_POINT_HEIGHT = 350

FPS = 60
REFRESH_RATE = int(1000 / FPS)

SIDEBAR_WIDTH = DEFAULT_WIDTH * 0.1875
SEPARATION_LINE_WIDTH = 5
SIDEBAR_POINTS_HEIGHT = 50

# Colors
C_MAIN = "#EDE6E3"
C_SECONDARY = "#202941"
C_ACCENT = "#B8BEDD"
C_TEXT = "#36382E"
C_SEPARATION_LINE = "#FFF"

F_CALIBRI = ("Calibri", 15)
F_POINTS_COMBOBOX = ("Calibri", 19)

DEFAULT_CENTER_X = 5
DEFAULT_CENTER_Y = 5
PARAM_WIDTH = 20

DEFAULT_POINTS = [
    Point(4, 9.6, 3, -0.1),
    Point(8.6, 8, -3, -3.5),
    Point(8.2, 4.6, 2.5, -0.5),
    Point(9.4, 5.4, 0.4, -3),
    Point(8, 3.2, -5, 0),
    Point(6, 2, 1, -3),
    Point(2.5, 2, -2, 2),
    Point(2, 7, 2, 1.5),
    Point(6, 7, -0.4, 1),
    Point(4, 9.6, 3, -0.1)
]

# points = [
#     [4, 9.6],
#     [8.6, 8],
#     [8.2, 4.6],
#     [9.4, 5.4],
#     [8, 3.2],
#     [6, 2],
#     [2.5, 2],
#     [2, 7],
#     [6, 7],
#     [4, 9.6]
# ]

# slopes = [
#     [3, -0.1],
#     [-3, -3.5],
#     [2.5, -0.5],
#     [0.4, -3],
#     [-5, 0],
#     [1, -3],
#     [-2, 2],
#     [2, 1.5],
#     [-0.4, 1],
#     [3, -0.1]
# ]

# centerPoint = [15, 15]

# precision = 50

# intervalLength = 30

# drawPoints = True
# drawSlopes = True
# drawCenteredReplica = True
# interpolateAbscissas = True
# symmetry = True
# xSymmetry = True
# ySymmetry = True