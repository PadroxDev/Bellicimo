class Point:
    def __init__(self, x: float = 0, y: float = 0, slopeX: float = 0, slopeY: float = 0):
        self.x = x
        self.y = y
        self.slopeX = slopeX
        self.slopeY = slopeY

    def __str__(self):
        return "P({0:.1f}, {1:.1f}, {2:.1f}, {3:.1f})".format(self.x, self.y, self.slopeX, self.slopeY)