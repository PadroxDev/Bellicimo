import tkinter as tk
from tkinter import ttk

from constants import *

class HermiteParams:
    def __init__(self, points: list=DEFAULT_POINTS):
        self.points = points
        self.centerX = tk.IntVar()
        self.centerY = tk.IntVar()
        self.precision = tk.IntVar()
        self.intervalLength = tk.IntVar()
        self.drawPoints = tk.IntVar()
        self.drawSlopes = tk.IntVar()
        self.drawCenteredReplica = tk.IntVar()
        self.interpolateAbscissas = tk.IntVar()
        self.symmetry = tk.IntVar()
        self.xSymmetry = tk.IntVar()
        self.ySymmetry = tk.IntVar()